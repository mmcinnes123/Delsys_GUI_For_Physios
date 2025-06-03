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

class PlottingManagement():
    def __init__(self, collect_data_window, metrics, emgplot=None):
        self.base = TrignoBase(self)
        self.collect_data_window = collect_data_window
        self.EMGplot = emgplot
        self.metrics = metrics
        self.packetCount = 0  # Number of packets received from base
        self.pauseFlag = True  # Flag to start/stop collection and plotting
        self.DataHandler = DataKernel(self.base)  # Data handler for receiving data from base
        self.base.DataHandler = self.DataHandler
        self.outData = [[0]]
        self.Index = None
        self.newTransform = None

        self.streamYTData = False # set to True to stream data in (T, Y) format (T = time stamp in seconds Y = sample value)

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

            self.updatemetrics()

    def streamingYT(self):
        """This is the data processing thread"""
        self.emg_queue = deque()
        while self.pauseFlag is True:
            continue
        while self.pauseFlag is False:
            self.DataHandler.processYTData(self.emg_plot)
            self.updatemetrics()

    def myIMUdata(self):
        while self.pauseFlag is False:
            if len(self.emg_plot) >= 2:
                incData = self.emg_plot.popleft()  # Returns the oldest element in the deque
                try:
                    self.outData = list(np.asarray(incData, dtype='object')[tuple([self.base.oriChannelsIdx])]) # Gets the elements of incData that matches channel IDs
                except IndexError:
                    print("Index Error Occurred: vispyPlot()")

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

    def vispyPlot(self):
        """Plot Thread - Only Plotting EMG Channels"""
        while self.pauseFlag is False:
            if len(self.emg_plot) >= 2:
                incData = self.emg_plot.popleft()  # Returns the oldest element in the deque
                print(f'MARZ - len of incData firect element: {len(incData[0])}')
                # print(f'MARZ - emgChannelsIdx{tuple([self.base.emgChannelsIdx])}')
                try:
                    self.outData = list(np.asarray(incData, dtype='object')[tuple([self.base.emgChannelsIdx])]) # Gets the elements of incData that matches channel IDs
                except IndexError:
                    print("Index Error Occurred: vispyPlot()")

                # print('MARZ - emgChannelsIdx: ', self.base.emgChannelsIdx)
                if self.base.emgChannelsIdx and len(self.outData[0]) > 0:
                    try:
                        self.EMGplot.plot_new_data(self.outData,
                                                   [self.emg_plot[0][i][0] for i in self.base.emgChannelsIdx])
                    except IndexError:
                        print("Index Error Occurred: vispyPlot()")

    def updatemetrics(self):
        self.metrics.framescollected.setText(str(self.DataHandler.packetCount))
        self.metrics.myMetric.setText(str(self.DataHandler.myQuat))

    def resetmetrics(self):
        self.metrics.framescollected.setText("0")
        self.metrics.totalchannels.setText(str(self.base.channelcount))

    def threadManager(self, start_trigger, stop_trigger):
        """Handles the threads for the DataCollector gui"""
        self.emg_plot = deque()

        # Start standard data stream (only channel data, no time values)
        if not self.streamYTData:
            self.t1 = threading.Thread(target=self.streaming)
            self.t1.start()

        # Start YT data stream (with time values)
        else:
            self.t1 = threading.Thread(target=self.streamingYT)
            self.t1.start()

        if self.EMGplot:
            self.t2 = threading.Thread(target=self.vispyPlot)
            if not start_trigger:
                self.t2.start()

        if start_trigger:
            self.t3 = threading.Thread(target=self.waiting_for_start_trigger)
            self.t3.start()

        if stop_trigger:
            self.t4 = threading.Thread(target=self.waiting_for_stop_trigger)
            self.t4.start()

        self.t5 = threading.Thread(target=self.myIMUdata)
        self.t5.start()

    def waiting_for_start_trigger(self):
        while self.base.TrigBase.IsWaitingForStartTrigger():
            continue
        self.pauseFlag = False
        if self.EMGplot:
            self.t2.start()
        print("Trigger Start - Collection Started")

    def waiting_for_stop_trigger(self):
        while self.base.TrigBase.IsWaitingForStartTrigger():
            continue
        while self.base.TrigBase.IsWaitingForStopTrigger():
            continue
        self.pauseFlag = True
        self.metrics.pipelinestatelabel.setText(self.PipelineState_Callback())
        print("Trigger Stop - Data Collection Complete")
        self.DataHandler.processData(self.emg_plot)
