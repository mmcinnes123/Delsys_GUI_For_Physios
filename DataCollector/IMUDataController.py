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

class IMUPlottingManagement():
    def __init__(self, live_data_window, collect_window):
        self.base = TrignoBase(self)
        self.live_data_window = live_data_window
        self.collect_window = collect_window
        self.live_window_metrics = live_data_window.MetricsConnector
        self.collect_window_metrics = collect_window.MetricsConnector
        self.packetCount = 0  # Number of packets received from base
        self.pauseFlag = True  # Flag to start/stop collection and plotting (controlled in Base start and stop callbacks)
        self.DataHandler = DataKernel(self.base)  # Data handler for receiving data from base
        self.base.DataHandler = self.DataHandler
        self.outData = [[0]]
        self.Index = None
        self.newTransform = None
        self.live_window_plot = live_data_window.plotCanvas
        self.collect_window_plot = collect_window.plotCanvas
        self.vis_data = False   # Flag whether vis data window is open or not

        self.streamYTData = False # set to True to stream data in (T, Y) format (T = time stamp in seconds Y = sample value)


    def streaming(self):
        """This is the data processing thread"""
        while self.pauseFlag is True:   # Wait for base start callback
            continue
        while self.pauseFlag is False:
            self.DataHandler.processData(self.data_deque) # Get packets of data from the base and append to the queue


    # TODO: Write STOP somewhere which checks three sensors are connected before running any of this

    def sensor_data_check(self):

        if not self.collect_window_plot.is_initialized:
            self.collect_window_plot.initiateCanvas()  # Make sure the canvas is initialized

        while self.vis_data is False and self.pauseFlag is False:    # This thread (while loop) should stop when vis data window is closed
            if len(self.data_deque) >= 2:
                incData = self.data_deque.popleft()  # Returns the oldest element in the deque and removes it from data_deque
                try:
                    self.outData = list(np.asarray(incData, dtype='object')[tuple([self.base.oriChannelsIdx])]) # Gets the elements of incData that matches channel IDs
                except IndexError:
                    print("Index Error Occurred: vispyPlot()")

                self.my_quat = self.outData[0][0]

                all_sensor_quats = self.getQuatsfromOutData(self.outData)
                if len(all_sensor_quats) == 1:
                    s1_quat = all_sensor_quats
                elif len(all_sensor_quats) == 2:
                    s1_quat, s2_quat = all_sensor_quats
                elif len(all_sensor_quats) == 3:
                    s1_quat, s2_quat, s3_quat = all_sensor_quats
                else:
                    print("Warning: Only {(max_index + 1)/2} sensors connected")
                    continue

                # Get relative orientation of two sensors
                # elbow_quat = qmt.qrel(s2_quat, s3_quat)
                # elbow_euls = np.rad2deg(qmt.eulerAngles(elbow_quat, axes='zxy'))

                # Express IMU1 ori as Euler angles and plot
                self.s1_eul = np.rad2deg(qmt.eulerAngles(all_sensor_quats[0], axes='zyx'))
                # self.collect_window_plot.plot_new_data(self.s1_eul)

                # Plot static numbers
                self.collect_window_plot.plot_new_data(np.array([0.0, 45.0, 90.0]))

                self.updatemetrics()


    def updatemetrics(self):
        self.live_window_metrics.myMetric.setText(f"{self.my_quat:.2f}")
        self.collect_window_metrics.framescollected.setText(str(self.DataHandler.packetCount))

    def resetmetrics(self):
        self.collect_window_metrics.framescollected.setText("0")  # Reset collect data window metrics
        self.collect_window_metrics.totalchannels.setText(str(self.base.channelcount))  # Reset collect data window metrics

    def threadManager(self, start_trigger, stop_trigger):
        """Handles the threads for the DataCollector gui"""
        self.data_deque = deque()     # Create a new, empty double-ended queue

        # Start standard data stream (only channel data, no time values)
        self.t1 = threading.Thread(target=self.streaming)
        print('Starting streaming thread...')
        self.t1.start()

        self.t2 = threading.Thread(target=self.sensor_data_check)
        print('Starting sensor_data_check thread...')
        self.t2.start()


    def getQuatsfromOutData(self, outData):

        sensor_indices = [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11)]  # Indices for s1, s2, s3
        all_sensor_quats = []
        max_index = len(outData) - 1

        for i, indices in enumerate(sensor_indices):
            if max(indices) <= max_index:
                try:
                    quat = qmt.normalized(np.array([self.outData[j][0] for j in indices]))
                    all_sensor_quats.append(quat)
                except IndexError:
                    print(f'Warning: Only {(max_index + 1)/2} sensors connected')
                    continue

        return all_sensor_quats

