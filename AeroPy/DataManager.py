"""
This is the class that handles the data that is output from the Delsys Trigno Base.
Create an instance of this and pass it a reference to the Trigno base for initialization.
See CollectDataController.py for a usage example.
"""
import numpy as np


class DataKernel():
    def __init__(self, trigno_base):
        self.trigno_base = trigno_base
        self.TrigBase = trigno_base.TrigBase
        self.packetCount = 0
        self.sampleCount = 0
        self.allcollectiondata = []
        self.channel1time = []
        self.channel_guids = []
        self.myQuat = [1, 0, 0, 0]

    def processData(self, data_queue):
        """Processes the data from the DelsysAPI and place it in the data_queue argument"""
        outArr = self.GetData()
        if outArr is not None:

            # # # Shape of outArr
            # print(f"Number of channels in outArr: {len(outArr)}")   # This is 9 for this sensor mode (4 EMG, 4 quats, 'IMU accuracy')
            # if len(outArr) > 4 and len(outArr[0]) > 0:
            #     print(f'MARZ - outArr: {outArr}')
            #     print(f'outArr[4]: {outArr[4]}')    # First quat channel (a list of length 1, containing an array packet with 2 values of that variable (packet of 2)).
            #     print(f'outArr[4][0]: {outArr[4][0]}') # The first element of the list (i.e., the array with 2 values of that variable (packet of 2)).
            #     print(f'outArr[4][0][0]: {outArr[4][0][0]}')  # The first value of the array (i.e., the first value of the packet of 2).

            # Currently disabled since we don't need to store the data
            # for i in range(len(outArr)):
                # self.allcollectiondata[i].extend(outArr[i][0].tolist()) # This appends the whole packet of each channel to the list

            try:
                for i in range(len(outArr[0])):
                    if np.asarray(outArr[0]).ndim == 1:     # If outArr is None
                        data_queue.append(list(np.asarray(outArr, dtype='object')[0]))
                    else:
                        data_queue.append(list(np.asarray(outArr, dtype='object')[:, i])) # Appending a list of 9 arrays, where each array has a packet of data
                try:
                    # self.myQuat = outArr[4][0][0]
                    self.packetCount += len(outArr[0])
                    self.sampleCount += len(outArr[0][0])
                except:
                    pass
            except IndexError:
                pass

    def processYTData(self, data_queue):
        """Processes the data from the DelsysAPI and place it in the data_queue argument"""
        outArr = self.GetYTData()
        if outArr is not None:
            for i in range(len(outArr)):
                self.allcollectiondata[i].extend(outArr[i][0].tolist())
            try:
                yt_outArr = []
                for i in range(len(outArr)):
                    chan_yt = outArr[i]
                    chan_ydata = np.asarray([k.Item2 for k in chan_yt[0]], dtype='object')
                    yt_outArr.append(chan_ydata)

                data_queue.append(list(yt_outArr))

                try:
                    self.packetCount += len(outArr[0])
                    self.sampleCount += len(outArr[0][0])
                except:
                    pass
            except IndexError:
                pass

    def GetData(self):
        """ Check if data ready from DelsysAPI via Aero CheckDataQueue() - Return True if data is ready
            Get data (PollData)
            Organize output channels by their GUID keys

            Return array of all channel data
        """

        dataReady = self.TrigBase.CheckDataQueue()                      # Check if DelsysAPI real-time data queue is ready to retrieve
        if dataReady:
            try:
                DataOut = self.TrigBase.PollData()                          # Dictionary<Guid, List<double>> (key = Guid (Unique channel ID), value = List(Y) (Y = sample value)
                if len(list(DataOut.Keys)) > 0:
                    outArr = [[] for i in range(len(self.trigno_base.channel_guids))]             # Set output array size to the amount of channels set during ConfigureCollectionOutput() in TrignoBase.py

                    for j in range(len(self.trigno_base.channel_guids)):            #Loop all channels set during configuration (default behavior is all channels unless updated)
                        chan_data = DataOut[self.trigno_base.channel_guids[j]]      # Index a single channels data from the dictionary based on unique channel GUID (key)
                        outArr[j].append(np.asarray(chan_data, dtype='object'))     # Create a NumPy array of the channel data and add to the output array

                    return outArr
            except Exception as e:
                print("Exception occured in GetData() - " + str(e))
        else:
            return None

    def GetYTData(self):
        """ YT Data stream only available when passing 'True' to Aero Start() command i.e. TrigBase.Start(True)
            Check if data ready from DelsysAPI via Aero CheckYTDataQueue() - Return True if data is ready
            Get data (PollYTData)
            Organize output channels by their GUID keys

            Return array of all channel data
        """

        dataReady = self.TrigBase.CheckYTDataQueue()                        # Check if DelsysAPI real-time data queue is ready to retrieve
        if dataReady:
            try:
                DataOut = self.TrigBase.PollYTData()                            # Dictionary<Guid, List<(double, double)>> (key = Guid (Unique channel ID), value = List<(T, Y)> (T = time stamp in seconds Y = sample value)
                if len(list(DataOut.Keys)) > 0:
                    outArr = [[] for i in range(len(self.trigno_base.channel_guids))]  # Set output array size to the amount of channels set during ConfigureCollectionOutput() in TrignoBase.py

                    for j in range(len(self.trigno_base.channel_guids)):            #Loop all channels set during configuration (default behavior is all channels unless updated)
                        chan_yt_data = DataOut[self.trigno_base.channel_guids[j]]    # Index a single channels data from the dictionary based on unique channel GUID (key)
                        outArr[j].append(np.asarray(chan_yt_data, dtype='object'))  # Create a NumPy array of the channel data and add to the output array

                    return outArr

            except Exception as e:
                print("Exception occured in GetYTData() - " + str(e))
        else:
            return None
