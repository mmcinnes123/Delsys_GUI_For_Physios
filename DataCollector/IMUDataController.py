"""
Controller class for the Data Collector GUI
This is the controller for the GUI that lets you connect to a base, scan via rf for sensors, and stream data from them in real time.
"""

from collections import deque

from Plotter.GenericPlot import *
from AeroPy.TrignoBase import *
from AeroPy.DataManager import *

clr.AddReference("System.Collections")

app.use_app('PySide6')

# Test commit

class IMUPlottingManagement():
    def __init__(self, data_window, metrics, plot_canvas):
        self.base = TrignoBase(self)
        print('Base has been called with IMUPlottingManagement as the data_collection_handler argument.')
        self.data_window = data_window
        self.metrics = metrics
        self.packetCount = 0  # Number of packets received from base
        self.pauseFlag = True  # Flag to start/stop collection and plotting
        self.DataHandler = DataKernel(self.base)  # Data handler for receiving data from base
        self.base.DataHandler = self.DataHandler
        self.outData = [[0]]
        self.Index = None
        self.newTransform = None
        self.myQuat = 0

        self.streamYTData = False # set to True to stream data in (T, Y) format (T = time stamp in seconds Y = sample value)
        self.EMGplot = False

    def streaming(self):
        """This is the data processing thread"""
        self.emg_queue = deque()
        while self.pauseFlag is True:
            continue
        while self.pauseFlag is False:
            self.DataHandler.processData(self.emg_plot)
            # if self.emg_plot:  # checks if deque is not empty
            #     print(f'emg_plot length: {len(self.emg_plot)}')
            #     # print(f'Last element: {self.emg_plot[-1]}')
            # else:
            #     print('emg_plot is empty')


    def myIMUdata(self):
        while self.pauseFlag is False:
            if len(self.emg_plot) >= 2:
                incData = self.emg_plot.popleft()  # Returns the oldest element in the deque
                try:
                    self.outData = list(np.asarray(incData, dtype='object')[tuple([self.base.oriChannelsIdx])]) # Gets the elements of incData that matches channel IDs
                except IndexError:
                    print("Index Error Occurred: vispyPlot()")

                self.my_quat = self.outData[0][0]
                self.updatemetrics()

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
        print('Updating metrics... ')
        self.metrics.myMetric.setText('This')
        # self.metrics.myMetric.setText(str(self.myQuat))

    def resetmetrics(self):
        self.metrics.framescollected.setText("0")
        self.metrics.totalchannels.setText(str(self.base.channelcount))

    def threadManager(self, start_trigger, stop_trigger):
        """Handles the threads for the DataCollector gui"""
        self.emg_plot = deque()

        # Start standard data stream (only channel data, no time values)
        self.t1 = threading.Thread(target=self.streaming)
        print('Starting streaming thread...')
        self.t1.start()

        self.t5 = threading.Thread(target=self.myIMUdata)
        print('Starting myIMUdata thread...')
        self.t5.start()

