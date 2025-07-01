"""
This class creates an instance of the Trigno base. Put your key and license here.
"""
import threading
import time
from pythonnet import load

from Export.CsvWriter import CsvWriter

load("coreclr")
import clr
import csv

clr.AddReference("resources\DelsysAPI")
clr.AddReference("System.Collections")

from Aero import AeroPy

key = "MIIBKjCB4wYHKoZIzj0CATCB1wIBATAsBgcqhkjOPQEBAiEA/////wAAAAEAAAAAAAAAAAAAAAD///////////////8wWwQg/////wAAAAEAAAAAAAAAAAAAAAD///////////////wEIFrGNdiqOpPns+u9VXaYhrxlHQawzFOw9jvOPD4n0mBLAxUAxJ02CIbnBJNqZnjhE50mt4GffpAEIQNrF9Hy4SxCR/i85uVjpEDydwN9gS3rM6D0oTlF2JjClgIhAP////8AAAAA//////////+85vqtpxeehPO5ysL8YyVRAgEBA0IABAtCPo3o5CG3ywtG9XmM8Itf9GN/oIxkYfRYLnDZvLqIcMTjMTFG0f7jE/W6RQKa1fo+zVNTmEUQaWxAP5K/W+k="
license = "<License>  <Id>4c37b4bf-188b-4f02-8903-676a32c02b10</Id>  <Type>Standard</Type>  <Quantity>10</Quantity>  <LicenseAttributes>    <Attribute name='Software'></Attribute>  </LicenseAttributes>  <ProductFeatures>    <Feature name='Sales'>True</Feature>    <Feature name='Billing'>False</Feature>  </ProductFeatures>  <Customer>    <Name>University of Aberdeen</Name>    <Email>edward.chadwick@abdn.ac.uk</Email>  </Customer>  <Expiration>Thu, 12 Jan 2034 00:00:00 GMT</Expiration>  <Signature>MEYCIQCTZkuDsiZ1GjIY8HQKXwRLquG1gQ9KDDRJRtIn/65XtgIhAMq0AD1PsSsTppcZIQWx1b0cjLkJgIh+Suh/A2GwefYF</Signature></License>"


class TrignoBase():
    """
    AeroPy reference imported above then instantiated in the constructor below
    All references to TrigBase. call an AeroPy method (See AeroPy documentation for details)
    """

    def __init__(self, collection_data_handler):
        self.TrigBase = AeroPy()
        self.collection_data_handler = collection_data_handler
        self.channel_guids = []
        self.channelcount = 0
        self.pairnumber = 0
        self.csv_writer = CsvWriter()

    # -- AeroPy Methods --
    def PipelineState_Callback(self):
        return self.TrigBase.GetPipelineState()

    def Connect_Callback(self):
        """Callback to connect to the base"""
        self.TrigBase.ValidateBase(key, license)

    def Pair_Callback(self):
        return self.TrigBase.PairSensor(self.pair_number)

    def CheckPairStatus(self):
        return self.TrigBase.CheckPairStatus()

    def CheckPairComponentAdded(self):
        return self.TrigBase.CheckPairComponentAdded()

    def Scan_Callback(self):
        """Callback to tell the base to scan for any available sensors"""

        try:
            f = self.TrigBase.ScanSensors().Result
        except Exception as e:
            print("Warning: Scan failed")
            return []

        self.all_scanned_sensors = self.TrigBase.GetScannedSensorsFound()
        print("Sensors Found:\n")
        for sensor in self.all_scanned_sensors:
            sensorStickerNumber = str(sensor.PairNumber + 1)
            print("(" + sensorStickerNumber + ") " +
                sensor.FriendlyName + "\n")

        self.SensorCount = len(self.all_scanned_sensors)
        for i in range(self.SensorCount):
            self.TrigBase.SelectSensor(i)

        return self.all_scanned_sensors


    def Start_Callback(self, start_trigger, stop_trigger):
        """Callback to start the data stream from Sensors"""
        self.start_trigger = start_trigger
        self.stop_trigger = stop_trigger

        configured = self.ConfigureCollectionOutput()
        print(f'Sensor Ori Channels: {self.sensorOriChannels}')

        if configured:
            #(Optional) To get YT data output pass 'True' to Start method
            self.TrigBase.Start(self.collection_data_handler.streamYTData)
            self.collection_data_handler.threadManager(self.start_trigger, self.stop_trigger)

    def ConfigureCollectionOutput(self):
        if not self.start_trigger:
            self.collection_data_handler.pauseFlag = False

        self.collection_data_handler.DataHandler.packetCount = 0
        self.collection_data_handler.DataHandler.allcollectiondata = []


        # Pipeline Armed when TrigBase.Configure already called.
        # This if block allows for sequential data streams without reconfiguring the pipeline each time.
        # Reset output data structure before starting data stream again
        if self.TrigBase.GetPipelineState() == 'Armed':
            self.csv_writer.cleardata()
            for i in range(len(self.channelobjects)):
                self.collection_data_handler.DataHandler.allcollectiondata.append([])
            return True


        # Pipeline Connected when sensors have been scanned in sucessfully.
        # Configure output data using TrigBase.Configure and pass args if you are using a start and/or stop trigger
        elif self.TrigBase.GetPipelineState() == 'Connected':
            self.csv_writer.clearall()
            self.channelcount = 0
            self.TrigBase.Configure(self.start_trigger, self.stop_trigger)
            configured = self.TrigBase.IsPipelineConfigured()
            if configured:
                self.channelobjects = []
                self.plotCount = 0
                self.emgChannelsIdx = []
                self.oriChannelsIdx = []
                globalChannelIdx = 0
                self.channel_guids = []
                self.sensorOriChannels = {}
                self.connectedSensorStickerNos = []

                for i in range(self.SensorCount):

                    ori_channel_idx = []

                    selectedSensor = self.TrigBase.GetSensorObject(i)
                    # print("(" + str(selectedSensor.PairNumber) + ") " + str(selectedSensor.FriendlyName))

                    sensorStickerNumber = str(selectedSensor.PairNumber + 1)
                    self.connectedSensorStickerNos.append(sensorStickerNumber)

                    print(f'Sensor Sticker No: {selectedSensor.PairNumber + 1}'
                          f'\n Name: {selectedSensor.FriendlyName}'
                          f'\n Mode: {selectedSensor.Configuration.ModeString}'
                          f'\n Channels: {len(selectedSensor.TrignoChannels)}')

                    # CSV Export Config
                    self.csv_writer.appendSensorHeader(selectedSensor)

                    if len(selectedSensor.TrignoChannels) > 0:

                        for channel in range(len(selectedSensor.TrignoChannels)):
                            ch_object = selectedSensor.TrignoChannels[channel]
                            if str(ch_object.Type) == "SkinCheck":
                                continue

                            ch_guid = ch_object.Id
                            ch_type = str(ch_object.Type)
                            # print(f'Channel type: {ch_type}')

                            get_all_channels = True
                            if get_all_channels:
                                self.channel_guids.append(ch_guid)
                                globalChannelIdx += 1

                                if ch_type == 'ORIENTATION':
                                    ori_channel_idx.append(globalChannelIdx - 1)

                                # ---- Plot EMG Channels
                                if ch_type == 'EMG':
                                    self.emgChannelsIdx.append(globalChannelIdx - 1)

                                # ---- Exclude non-EMG channels from plots
                                else:
                                    pass

                                #CSV Export Config
                                if not self.collection_data_handler.streamYTData:
                                    self.csv_writer.appendChannelHeader(ch_object)
                                    if channel > 0 & channel != len(selectedSensor.TrignoChannels):
                                        self.csv_writer.appendSensorHeaderSeperator()
                                else:
                                    self.csv_writer.appendYTChannelHeader(ch_object)
                                    if channel == 0:
                                        self.csv_writer.appendSensorHeaderSeperator()
                                    elif channel > 0 & channel != len(selectedSensor.TrignoChannels):
                                        self.csv_writer.appendYTSensorHeaderSeperator()

                            #NOTE: The self.channel_guids list is used to parse select channels during live data streaming in DataManager.py
                            #      this example will add all available channels to this list (above)
                            #      if you want to only parse certain channels then add only those channel guids to this list
                            #      for example: if you only want the EMG channels during live data streaming (flip bool above to false):
                            if not get_all_channels:
                                if ch_type == 'EMG':
                                    self.channel_guids.append(ch_guid)
                                    self.csv_writer.h2_channels.append(
                                        ch_object.Name + " (" + str(ch_object.SampleRate) + ")")
                                    if channel > 0:
                                        self.csv_writer.h1_sensors.append(",")
                                    globalChannelIdx += 1

                            sample_rate = round(selectedSensor.TrignoChannels[channel].SampleRate, 3)
                            # print("----" + selectedSensor.TrignoChannels[channel].Name + " (" + str(sample_rate) + " Hz) " + str(selectedSensor.TrignoChannels[channel].Id))
                            self.channelcount += 1
                            self.channelobjects.append(channel)
                            self.collection_data_handler.DataHandler.allcollectiondata.append([])

                            # NOTE: Plotting/Data Output: This demo does not plot non-EMG channel types such as
                            # accelerometer, gyroscope, magnetometer, and others. However, the data from channels
                            # that are excluded from plots are still available via output from PollData()
                            #
                            # if ch_type == 'ORIENTATION':
                            #     self.oriChannelsIdx.append(globalChannelIdx-1)

                    # Save the sensor number and channel IDs for later use
                    self.sensorOriChannels[sensorStickerNumber] = ori_channel_idx


                return True
            return None
        else:
            return False

    def Stop_Callback(self):
        """Callback to stop the data stream"""
        self.collection_data_handler.pauseFlag = True
        print('Set Pause Flag to True')
        self.TrigBase.Stop()
        print("Data Collection Complete")
        self.csv_writer.data = self.collection_data_handler.DataHandler.allcollectiondata

    # ---------------------------------------------------------------------------------
    # ---- Helper Functions

    def getSampleModes(self, sensorIdx):
        """Gets the list of sample modes available for selected sensor"""
        sampleModes = self.TrigBase.AvailibleSensorModes(sensorIdx)
        return sampleModes

    def getCurMode(self, sensorIdx):
        """Gets the current mode of the sensors"""
        if sensorIdx >= 0 and sensorIdx <= self.SensorCount:
            curModes = self.TrigBase.GetCurrentSensorMode(sensorIdx)
            return curModes
        else:
            return None


    def setSampleMode(self, curSensor, setMode):
        """Sets the sample mode for the selected sensor"""
        self.TrigBase.SetSampleMode(curSensor, setMode)
        mode = self.getCurMode(curSensor)
        sensor = self.TrigBase.GetSensorObject(curSensor)
        stickerNumber = str(sensor.PairNumber + 1)
        if mode == setMode:
            print("\n(" + stickerNumber + ") " + str(sensor.FriendlyName) +" Mode Change Successful")