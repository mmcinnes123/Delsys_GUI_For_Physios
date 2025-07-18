"""
Controller class for the Data Collector GUI
This is the controller for the GUI that lets you connect to a base, scan via rf for sensors, and stream data from them in real time.
"""

from collections import deque
import time
import qmt

from Plotter.GenericPlot import *
from AeroPy.TrignoBase import *
from AeroPy.DataManager import *

clr.AddReference("System.Collections")

app.use_app('PySide6')

# TODO: Tidy this file into sections

class IMUDataController():
    def __init__(self, collect_window):
        self.base = TrignoBase(self)
        # self.live_data_window = live_data_window
        self.collect_window = collect_window
        # self.live_window_metrics = live_data_window.MetricsConnector
        self.collect_window_metrics = collect_window.ConnectMetricsConnector
        self.DataHandler = DataKernel(self.base)  # Data handler for receiving data from base
        self.base.DataHandler = self.DataHandler
        self.Index = None
        self.newTransform = None
        # self.live_window_plot = live_data_window.plotCanvas1
        self.collect_window_plot1 = collect_window.plotCanvas1
        self.collect_window_plot2 = collect_window.plotCanvas2
        self.collect_window_plot3 = collect_window.plotCanvas3

        self.vis_dataFlag = False   # Flags stop/start of data visualisation, set to True when data vis window is opened, and false when closed
        self.pauseFlag = True  # Flags start/stop of data collection. Set to false during base config, true during stop callback

        self.packetCount = 0  # Number of packets received from base
        self.incData = None
        self.outData = [[0]]
        self.sen1_quat = [1, 0, 0, 0]
        self.sen2_quat = [1, 0, 0, 0]
        self.sen3_quat = [1, 0, 0, 0]
        self.el_flex_max = 0
        self.el_ext_max = 90
        self.el_pro_max = 0
        self.el_sup_max = 0
        self.sh_flex_max = 0
        self.sh_abd_max = 0
        self.sh_introt_max = 0
        self.sh_extrot_max = 0
        self.conf_sensorOriChannels = {}

        self.streamYTData = False # set to True to stream data in (T, Y) format (T = time stamp in seconds Y = sample value)

    # -----------------------------------------------------------------------
    # ---- Threads

    def streaming(self):
        """This thread gets the data from the base and appends it to the deque"""

        while self.pauseFlag is True:   # Wait for base start callback
            continue

        while self.pauseFlag is False:
            self.DataHandler.processData(self.data_deque) # Get packets of data from the base and append to the queue
            self.updateCollectMetrics()

            # Extract quaternion values from the deque
            if len(self.data_deque) >= 2:
                self.incData = self.data_deque.popleft()  # Returns the oldest element in the deque and removes it from data_deque

    def processData(self):
        """ This thread processes the data.
        It gets the sensor orientation data from the incData
        and gets joint angle data when data vis window is open."""

        while self.pauseFlag is True:  # Wait for base start callback
            continue

        while self.pauseFlag is False:
            if self.incData is not None:

                # Get the sensor orientation data from the incData
                if all(str(i) in self.conf_sensorOriChannels for i in ['1', '2', '3']):
                    self.sen1_quat = self.get_qmt_quat_from_incData('1')
                    self.sen2_quat = self.get_qmt_quat_from_incData('2')
                    self.sen3_quat = self.get_qmt_quat_from_incData('3')
                    self.updateSensorCheckMetrics()
                else:
                    print('Not all of Sensor 1, 2, and 3 are connected.')

                # Get the joint angle info from sensor orientations
                if self.vis_dataFlag is True:
                    self.getJointAngles()

            time.sleep(0.01)

    # ---- Sensor data plotting threads
    def plot_sensor1_data_check(self):

        while self.pauseFlag is True:   # Wait for base start callback
            time.sleep(0.1)
            continue

        while self.pauseFlag is False:  # Keep this thread running until base stop callback is called

            while self.vis_dataFlag is False and self.pauseFlag is False:   # Plot sensor data only when data vis window is not open
                if '1' in self.conf_sensorOriChannels:  # Plot IMU PRY data if it exists in the data channels
                    self.collect_window_plot1.plot_new_data(np.rad2deg(qmt.eulerAngles(self.sen1_quat, axes='zyx')))

            time.sleep(0.01)  # Add small delay to prevent CPU hogging

    def plot_sensor2_data_check(self):

        while self.pauseFlag is True:  # Wait for base start callback
            time.sleep(0.1)
            continue

        while self.pauseFlag is False:  # Keep this thread running until base stop callback is called

            while self.vis_dataFlag is False and self.pauseFlag is False:  # Plot sensor data only when data vis window is not open
                if '2' in self.conf_sensorOriChannels:  # Plot IMU PRY data if it exists in the data channels
                    self.collect_window_plot2.plot_new_data(np.rad2deg(qmt.eulerAngles(self.sen2_quat, axes='zyx')))

            time.sleep(0.01)  # Add small delay to prevent CPU hogging

    def plot_sensor3_data_check(self):

        while self.pauseFlag is True:  # Wait for base start callback
            time.sleep(0.1)
            continue

        while self.pauseFlag is False:  # Keep this thread running until base stop callback is called

            while self.vis_dataFlag is False and self.pauseFlag is False:  # Plot sensor data only when data vis window is not open
                if '3' in self.conf_sensorOriChannels:  # Plot IMU PRY data if it exists in the data channels
                    self.collect_window_plot3.plot_new_data(np.rad2deg(qmt.eulerAngles(self.sen3_quat, axes='zyx')))

            time.sleep(0.01)  # Add small delay to prevent CPU hogging

    # -----------------------------------------------------------------------
    # ---- Update Functions

    def updateSensorCheckMetrics(self):
        self.sen1_euls = np.rad2deg(qmt.eulerAngles(self.sen1_quat, axes='zyx'))
        self.sen2_euls = np.rad2deg(qmt.eulerAngles(self.sen2_quat, axes='zyx'))
        self.sen3_euls = np.rad2deg(qmt.eulerAngles(self.sen3_quat, axes='zyx'))

        self.collect_window_metrics.sen1eul1.setText(f"{self.sen1_euls[0]:.0f}°")
        self.collect_window_metrics.sen1eul2.setText(f"{self.sen1_euls[1]:.0f}°")
        self.collect_window_metrics.sen1eul3.setText(f"{self.sen1_euls[2]:.0f}°")
        self.collect_window_metrics.sen2eul1.setText(f"{self.sen2_euls[0]:.0f}°")
        self.collect_window_metrics.sen2eul2.setText(f"{self.sen2_euls[1]:.0f}°")
        self.collect_window_metrics.sen2eul3.setText(f"{self.sen2_euls[2]:.0f}°")
        self.collect_window_metrics.sen3eul1.setText(f"{self.sen3_euls[0]:.0f}°")
        self.collect_window_metrics.sen3eul2.setText(f"{self.sen3_euls[1]:.0f}°")
        self.collect_window_metrics.sen3eul3.setText(f"{self.sen3_euls[2]:.0f}°")


    def updateCollectMetrics(self):
        self.collect_window_metrics.framescollected.setText(str(self.DataHandler.packetCount))


    def resetmetrics(self):
        self.collect_window_metrics.framescollected.setText("0")  # Reset collect data window metrics
        self.collect_window_metrics.totalchannels.setText(str(self.base.channelcount))  # Reset collect data window metrics


    # -----------------------------------------------------------------------
    # ---- Thread manager

    def threadManager(self, start_trigger, stop_trigger):
        """Handles the threads for collecting and plotting data."""

        self.data_deque = deque()     # Create a new, empty double-ended queue

        # This is a dict which holds the channels indexs associated with each sensor ( e.g. {'1', [0, 1, 2, 3]} )
        self.conf_sensorOriChannels = self.base.sensorOriChannels

        # Initialise plots
        self.collect_window_plot1.initiateCanvas(10000)  # Make sure the canvas is initialized
        self.collect_window_plot2.initiateCanvas(10000)  # Make sure the canvas is initialized
        self.collect_window_plot3.initiateCanvas(10000)  # Make sure the canvas is initialized

        # Threads

        self.t1 = threading.Thread(target=self.streaming)
        print('Starting streaming thread...')
        self.t1.start()

        self.t5 = threading.Thread(target=self.processData)
        print('Starting processData thread...')
        self.t5.start()

        self.t2 = threading.Thread(target=self.plot_sensor1_data_check)
        print('Starting plot_sensor1_data_check thread...')
        self.t2.start()

        self.t3 = threading.Thread(target=self.plot_sensor2_data_check)
        print('Starting plot_sensor2_data_check thread...')
        self.t3.start()

        self.t4 = threading.Thread(target=self.plot_sensor3_data_check)
        print('Starting plot_sensor3_data_check thread...')
        self.t4.start()

    # -----------------------------------------------------------------------
    # ---- Orientation/Kinematic Functions

    def getJointAngles(self):
        """ Updates joint angles and max joint angles from sensor orientation data."""

        # Get body segment frames from sensor orientation data based on manual unit alignment
        self.thorax_quat = self.get_body_frames_from_sensor_frame(self.sen1_quat, body_name='thorax')
        self.humerus_quat = self.get_body_frames_from_sensor_frame(self.sen2_quat, body_name='humerus')
        self.forerarm_quat = self.get_body_frames_from_sensor_frame(self.sen3_quat, body_name='forearm')

        # Get joint doFs from body segment frames
        self.el_FE, self.el_CA, self.el_PS = self.get_elbow_DoFs_from_body_frames(self.humerus_quat, self.forerarm_quat)
        self.sh_EA, self.sh_IE, self.sh_PoE = self.get_shoulder_angles_from_body_frames(self.thorax_quat, self.humerus_quat)

        # Get joint angles from joint DoFs
        self.el_flex = self.el_FE
        self.el_ext = self.el_FE
        self.sh_abd = self.sh_EA
        self.sh_flex = self.sh_EA
        self.sh_introt = self.sh_IE
        self.sh_extrot = -self.sh_IE

        # Adjust these to match clinical definitions of PS
        if self.el_PS > 0:
            self.el_sup = 180 - self.el_PS - 90
        else:
            self.el_sup = abs(self.el_PS) + 90

        if self.el_PS > 0:
            self.el_pro = self.el_PS - 90
        else:
            self.el_pro = 180 - abs(self.el_PS) + 90

        # Apply constraints to discount certain angles in certain positions
        self.applyConstraints()

        # Update max value
        self.update_max_joint_angle_values()

    def get_qmt_quat_from_incData(self, senLabel):

        # Gets the elements of incData that matches channel Idx with each sensors orientation data
        outData = list(np.asarray(self.incData, dtype='object')[tuple([self.conf_sensorOriChannels[senLabel]])])

        # Get the four elements of the quaternion
        quat = np.array([outData[j][0] for j in [0, 1, 2, 3]])
        quat_norm = qmt.normalized(quat)

        return quat_norm

    def get_body_frames_from_sensor_frame(self, sensor_quat, body_name):

        # Transformation matrics to transform sensor local frames to match ISB body frames (specific to choice of placement)
        thorax_trans_quat = qmt.quatFromRotMat([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
        humerus_trans_quat = qmt.quatFromRotMat([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
        forearm_trans_quat = qmt.quatFromRotMat([[0, 0, -1], [0, -1, 0], [-1, 0, 0]])
        trans_quat = {'thorax': thorax_trans_quat, 'humerus': humerus_trans_quat, 'forearm': forearm_trans_quat}[body_name]

        body_quat = qmt.qmult(sensor_quat, trans_quat)

        return body_quat

    def get_elbow_DoFs_from_body_frames(self, humerus_quat, forearm_quat):

        elbow_joint = qmt.qmult(qmt.qinv(humerus_quat), forearm_quat)

        FE_ISB, CA_ISB, PS_ISB = np.rad2deg(qmt.eulerAngles(elbow_joint, axes='zxy'))   # Get joint eulers matching ISB definitions

        return FE_ISB, CA_ISB, PS_ISB

    def get_shoulder_angles_from_body_frames(self, thorax_quat, humerus_quat):

        shoulder_joint = qmt.qmult(qmt.qinv(thorax_quat), humerus_quat)

        # Get Euler angles for elevation angle
        shoulder_eulsISB = np.rad2deg(qmt.eulerAngles(shoulder_joint, axes='yxy'))

        sh_EA = shoulder_eulsISB[1]   # Shoudler elevation angle (This doesnt encounter gimbal lock)
        sh_PoE = shoulder_eulsISB[0]    # Shoulder plane of elevation (Encounters gimbal lock when sh_EA is near 0)

        # Get shoulder rotation from different Euler angle set
        shoudler_eulsYXZ = np.rad2deg(qmt.eulerAngles(shoulder_joint, axes='yxz'))
        sh_IE = shoudler_eulsYXZ[0]     # This encounters gimbal lock when elevation is near 90

        return sh_EA, sh_IE, sh_PoE

    def applyConstraints(self):

        # We are either in flexion (above 90) or extension (below 90)
        if self.el_FE > 90:
            self.el_ext = None
        if self.el_FE <= 90:
            self.el_flex = None

        # We are either in pronation (above 90) or supination (below 90)
        if 90 < self.el_PS or -90 > self.el_PS:
            self.el_sup = None
        if -90 < self.el_PS <= 90:
            self.el_pro = None

        # We are either in internal (above 0) or external rotation (below 0)
        if self.sh_IE < 0:
            self.sh_introt = None
        if self.sh_IE >= 0:
            self.sh_extrot = None

        # This measure of shoulder int/ext is only free of gimbal lock when elevation is low
        if self.sh_EA > 45:
            self.sh_introt = None
            self.sh_extrot = None

        if self.sh_EA > 25:
            if 0 > self.sh_PoE > -135:
                self.sh_abd = None
            else:
                self.sh_flex = None


    def update_max_joint_angle_values(self):

        if self.el_flex is not None:
            if self.el_flex > self.el_flex_max:
                self.el_flex_max = self.el_flex

        if self.el_ext is not None:
            if self.el_ext < self.el_ext_max:
                self.el_ext_max = self.el_ext

        if self.el_pro is not None:
            if self.el_pro > self.el_pro_max:
                self.el_pro_max = self.el_pro

        if self.el_sup is not None:
            if self.el_sup > self.el_sup_max:
                self.el_sup_max = self.el_sup

        if self.sh_flex is not None:
            if self.sh_flex > self.sh_flex_max:
                self.sh_flex_max = self.sh_flex

        if self.sh_abd is not None:
            if self.sh_abd > self.sh_abd_max:
                self.sh_abd_max = self.sh_abd

        if self.sh_introt is not None:
            if self.sh_introt > self.sh_introt_max:
                self.sh_introt_max = self.sh_introt

        if self.sh_extrot is not None:
            if self.sh_extrot > self.sh_extrot_max:
                self.sh_extrot_max = self.sh_extrot