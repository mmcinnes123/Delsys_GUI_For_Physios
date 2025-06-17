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
    def __init__(self, live_data_window, live_window_metrics, collect_window_metrics):
        self.base = TrignoBase(self)
        self.live_data_window = live_data_window
        self.metrics = live_window_metrics
        self.live_window_metrics = collect_window_metrics
        self.packetCount = 0  # Number of packets received from base
        self.pauseFlag = True  # Flag to start/stop collection and plotting (controlled in Base start and stop callbacks)
        self.DataHandler = DataKernel(self.base)  # Data handler for receiving data from base
        self.base.DataHandler = self.DataHandler
        self.outData = [[0]]
        self.Index = None
        self.newTransform = None
        self.EMGplot = live_data_window.plotCanvas

        self.streamYTData = False # set to True to stream data in (T, Y) format (T = time stamp in seconds Y = sample value)


    def streaming(self):
        """This is the data processing thread"""
        while self.pauseFlag is True:   # Wait for base start callback
            continue
        while self.pauseFlag is False:
            self.DataHandler.processData(self.data_deque) # Get packets of data from the base and append to the queue


    # TODO: Tidy up function below + Rename things in general to make sure everything's making sense

    def myIMUdata(self):

        if not self.EMGplot.is_initialized:
            self.EMGplot.initiateCanvas()  # Make sure the canvas is initialized

        while self.pauseFlag is False:
            if len(self.data_deque) >= 2:
                incData = self.data_deque.popleft()  # Returns the oldest element in the deque and removes it from data_deque
                try:
                    self.outData = list(np.asarray(incData, dtype='object')[tuple([self.base.oriChannelsIdx])]) # Gets the elements of incData that matches channel IDs
                except IndexError:
                    print("Index Error Occurred: vispyPlot()")

                self.my_quat = self.outData[0][0]

                all_sensor_quats = self.getQuatsfromOutData(self.outData)

                # Express IMU1 ori as Euler angles
                s1_eul = np.rad2deg(qmt.eulerAngles(all_sensor_quats[0], axes='zyx'))
                print(s1_eul.shape)
                self.updatemetrics()

                self.EMGplot.plot_new_data(self.my_quat)
                # my_counter = 0
                # while my_counter < 100:
                #     my_counter += 1
                #     print(f'outData: {self.outData}')
                #     print(f'Sensor 1 q_w: {self.outData[0][0]}')    # There's a packet of values in this array so we take the first one
                #     print(f'Sensor 1 q_x: {self.outData[1][0]}')
                #     print(f'Sensor 1 q_y: {self.outData[2][0]}')
                #     print(f'Sensor 1 q_z: {self.outData[3][0]}')
                #     print(f'Sensor 2 q_w: {self.outData[4][0]}')
                #     print(f'Sensor 2 q_x: {self.outData[5][0]}')
                #     print(f'Sensor 2 q_y: {self.outData[6][0]}')
                #     print(f'Sensor 2 q_z: {self.outData[7][0]}')
                #     print(f'Sensor 3 q_w: {self.outData[8][0]}')
                #     print(f'Sensor 3 q_x: {self.outData[9][0]}')
                #     print(f'Sensor 3 q_y: {self.outData[10][0]}')
                #     print(f'Sensor 3 q_z: {self.outData[11][0]}')

    def updatemetrics(self):
        self.metrics.myMetric.setText(f"{self.my_quat:.2f}")
        self.live_window_metrics.framescollected.setText(str(self.DataHandler.packetCount))

    def resetmetrics(self):
        self.live_window_metrics.framescollected.setText("0")  # Reset collect data window metrics
        self.live_window_metrics.totalchannels.setText(str(self.base.channelcount))  # Reset collect data window metrics

    def threadManager(self, start_trigger, stop_trigger):
        """Handles the threads for the DataCollector gui"""
        self.data_deque = deque()     # Create a new, empty double-ended queue

        # Start standard data stream (only channel data, no time values)
        self.t1 = threading.Thread(target=self.streaming)
        print('Starting streaming thread...')
        self.t1.start()

        self.t2 = threading.Thread(target=self.myIMUdata)
        print('Starting myIMUdata thread...')
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

