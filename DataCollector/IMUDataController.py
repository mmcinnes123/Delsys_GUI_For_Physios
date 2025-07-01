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

# Test commit

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

        self.vis_data = False   # Flags stop/start of data visualisation, set to True when data vis window is opened, and false when closed
        self.pauseFlag = True  # Flags start/stop of data collection. Set to false during base config, true during stop callback

        self.packetCount = 0  # Number of packets received from base
        self.outData = [[0]]
        self.sen1_quat = [1, 0, 0, 0]
        self.sen2_quat = [1, 0, 0, 0]
        self.sen3_quat = [1, 0, 0, 0]
        self.sen1_eul3_max = 0
        self.conf_sensorOriChannels = {}

        self.streamYTData = False # set to True to stream data in (T, Y) format (T = time stamp in seconds Y = sample value)


    def streaming(self):
        """This is the data processing thread"""

        while self.pauseFlag is True:   # Wait for base start callback
            continue

        while self.pauseFlag is False:
            self.DataHandler.processData(self.data_deque) # Get packets of data from the base and append to the queue
            self.updateCollectMetrics()

            # Extract values from the deque
            if len(self.data_deque) >= 2:
                incData = self.data_deque.popleft()  # Returns the oldest element in the deque and removes it from data_deque

                if all(str(i) in self.conf_sensorOriChannels for i in ['1', '2', '3']):
                    self.sen1_quat = self.get_qmt_quat_from_incData(incData, '1')
                    self.sen2_quat = self.get_qmt_quat_from_incData(incData, '2')
                    self.sen3_quat = self.get_qmt_quat_from_incData(incData, '3')
                    self.updateSensorCheckMetrics()

                else:
                    print('Not all of Sensor 1, 2, and 3 are connected.')

    # TODO: Take plot initialisation out of threads?
    # # TODO: Make sure plots stop when data vis starts and restart again when data vis stops

    def plot_sensor1_data_check(self):

        if not self.collect_window_plot1.is_initialized:
            self.collect_window_plot1.initiateCanvas(10000)  # Make sure the canvas is initialized

        while self.pauseFlag is True:   # Wait for base start callback
            continue

        while self.pauseFlag is False and self.vis_data is False:    # This thread (while loop) should stop when vis data window is closed

                # Plot dynamic value
                if '1' in self.conf_sensorOriChannels:
                    self.collect_window_plot1.plot_new_data(np.rad2deg(qmt.eulerAngles(self.sen1_quat, axes='zyx')))

    def plot_sensor2_data_check(self):

        if not self.collect_window_plot2.is_initialized:
            self.collect_window_plot2.initiateCanvas(10000)  # Make sure the canvas is initialized

        while self.vis_data is False and self.pauseFlag is False:    # This thread (while loop) should stop when vis data window is closed

                # Plot dynamic value
                if '2' in self.conf_sensorOriChannels:
                    self.collect_window_plot2.plot_new_data(np.rad2deg(qmt.eulerAngles(self.sen2_quat, axes='zyx')))

    def plot_sensor3_data_check(self):

        if not self.collect_window_plot3.is_initialized:
            self.collect_window_plot3.initiateCanvas(10000)  # Make sure the canvas is initialized

        while self.vis_data is False and self.pauseFlag is False:    # This thread (while loop) should stop when vis data window is closed

                # Plot dynamic value
                if '3' in self.conf_sensorOriChannels:
                    self.collect_window_plot3.plot_new_data(np.rad2deg(qmt.eulerAngles(self.sen3_quat, axes='zyx')))

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

        if self.sen1_euls[2] > self.sen1_eul3_max:
            self.sen1_eul3_max = self.sen1_euls[2]


    def updateCollectMetrics(self):
        self.collect_window_metrics.framescollected.setText(str(self.DataHandler.packetCount))

    def resetmetrics(self):
        self.collect_window_metrics.framescollected.setText("0")  # Reset collect data window metrics
        self.collect_window_metrics.totalchannels.setText(str(self.base.channelcount))  # Reset collect data window metrics

    def threadManager(self, start_trigger, stop_trigger):

        # This is a dict which holds the channels indexs associated with each sensor ( e.g. {'1', [0, 1, 2, 3]} )
        self.conf_sensorOriChannels = self.base.sensorOriChannels

        """Handles the threads for the DataCollector gui"""
        self.data_deque = deque()     # Create a new, empty double-ended queue

        # Start standard data stream (only channel data, no time values)
        self.t1 = threading.Thread(target=self.streaming)
        print('Starting streaming thread...')
        self.t1.start()

        self.t2 = threading.Thread(target=self.plot_sensor1_data_check)
        print('Starting sensor_data_check thread...')
        self.t2.start()

        self.t3 = threading.Thread(target=self.plot_sensor2_data_check)
        print('Starting sensor_data_check thread...')
        self.t3.start()

        self.t4 = threading.Thread(target=self.plot_sensor3_data_check)
        print('Starting sensor_data_check thread...')
        self.t4.start()

    def get_qmt_quat_from_incData(self, incData, senLabel):
        # Gets the elements of incData that matches channel Idx with each sensors orientation data
        outData = list(np.asarray(incData, dtype='object')[tuple([self.conf_sensorOriChannels[senLabel]])])
        # Get the four elements of the quaternion
        quat = qmt.normalized(np.array([outData[j][0] for j in [0, 1, 2, 3]]))
        return quat
