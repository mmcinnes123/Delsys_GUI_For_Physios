# DelsysAPI Python Example

Note: Mhairi's version run with Python 3.9.13. This made pip install qmt easier as there was .whl available for python version <3.11

This is an example Python GUI application that uses the DelsysAPI AeroPy Layer to demonstrate functionality that users can implement in their own code. This example allows a user to connect to the base station, pair new sensors, scan for paired sensors, then stream EMG data visualized by plots. 

This version has been tested using [Python 3.12.0](https://www.python.org/downloads/release/python-3120/).

See [AeroPy Documentation](#AeroPy-Documentation) 

## Getting Started
1. Install Python here: [Python 3.12.0](https://www.python.org/downloads/release/python-3120/).
2. Navigate to the `/Delsys-Python-Demo` base directory
3. Install dependencies using `python -m pip install -r requirements.txt`
4. Open `/AeroPy/TrignoBase.py` and copy/paste the key/license strings provided by Delsys Inc. during system purchase. Contact [support](https://delsys.com/support/) if you have any issues.
5. If you are using an IDE, set up your python interpreter/virtual environment from the settings.
6. Make sure the Trigno base station or lite are plugged in, then Run `DelsysPythonDemo.py`


## Example App Instructions

Ensure that your Trigno system is connected to power and the PC via USB. Click the `Connect` button to connect the app to the station.  In your terminal you will see some log and initialization messages.

Power on your sensor(s) by removing from the charge station and introducing a magnet. For convenience, the charge station has a magnet built in, under the "lock" symbol at the center of the case. If the sensor has not already been paired to the base, click the `Pair` button and introduce a magnet again to initiate a pair.

Click the `Scan` button. This will add your sensor to the application's sensor list. Highlight the sensor by clicking on it, then select its mode from the mode drop down menu. Setting modes is done to individual sensors, not all of them. If you want all of your sensors to be on the same mode, the code can be modified to achieve this. See [AeroPy Documentation](#AeroPy-Documentation) for more details.

To begin the data stream and plotting, click the `Start` button. To stop the data stream and plotting, click the `Stop` button.


## Further Reference
See the DelsysAPI Documentation [here](http://data.delsys.com/DelsysServicePortal/api/web-api/index.html).

## Navigation
[Python Setup](#Setup-(python)) &nbsp;<br>
[Connecting to the Trigno Base/Lite](#Connecting-to-the-Trigno-USB) &nbsp;<br>
[Sensor Management](#Sensor-Management) &nbsp;<br>
[Pre Data Collection Configuration](#Pre-Data-Collection-Configuration) &nbsp;<br>
[Data Collection Management](#Data-Collection-Management) &nbsp;<br>
[Helper Functions](#Helper-Functions) &nbsp;<br>
[DelsysAPI Object Properties](#DelsysAPI-Object-Properties) &nbsp;<br>



# AeroPy Documentation

The DelsysAPI and AeroPy software is a development tool to be used in conjunction
with the Trigno Wireless Biofeedback System. The DelsysAPI is not intended to perform assessment or
diagnostic procedures. It is intended to be used as a software component of a third-party
software application. The function of the API is to manage the transfer of data from the Trigno
System to third-party software applications, and is designed to work exclusively with the Trigno
System. AeroPy is a simplification layer of the DelsysAPI to facilitate easy setup for configuring and streaming from sensors.
See the list of AeroPy commands below.

## Setup (python)

The `DelsysAPI.dll` must be inside of the project folder ie. resources/

```python
"""
This class creates an instance of the Trigno base. Put your key and license here.
"""
import clr
clr.AddReference("/resources/DelsysAPI")
clr.AddReference("System.Collections")

from Aero import AeroPy

key = ""
license = ""

class TrignoBase():
    def __init__(self):
        self.BaseInstance = AeroPy()
```

```python
base = TrignoBase()
TrigBase = base.BaseInstance
```
Call TrignoBase class from your program script.

```python
    def Connect_Callback(self):
        """Callback to connect to the base"""
        TrigBase.ValidateBase(key, license)
```
Use TrigBase variable to call AeroPy functions. See all AeroPy methods below:

### Connecting to the Trigno USB
```C#
public void ValidateBase(string key, string license)
```
Initial call to the Trigno Base. Sets up a connection to the base using the user's key and license strings.

&nbsp;<br>

### Sensor Management
```C#
public Task ScanSensors()
```
Scan for previously paired sensors (RF).
Pipeline must be in the Off or Connected State to run this command 

&nbsp;<br> 

```C#
public SensorTrignoRf[] GetScannedSensorsFound()
```
Get an array of sensor objects for all Trigno sensors that were found during a scan. If your sensor is on but not found during a scan please pair the sensor first before scanning again. 

&nbsp;<br> 


```C#
public Task<bool> PairSensor()
```
This sets the base into pairing mode, allowing for a user to pair a new sensor to the base.
Pipeline must be in the Off or Connected State to run this command. Sensors only need to be paired to a specific base/lite one time.
Once a sensor has been paired, you will only need to turn on the sensor and begin a scan to connect it.

&nbsp;<br>

```C#
public Task<bool> PairSensor (int pairnumber)
```
This sets the base into pairing mode, allowing for a user to pair a new sensor to the base with a specific pair number.
Pipeline must be in the Off or Connected State to run this command. Sensors only need to be paired to a specific base/lite one time.
Once a sensor has been paired, you will only need to turn on the sensor and begin a scan to connect it. To update the pair number you must re-pair that sensor with the new pair number.

<ins>Basic Pairing in Python</ins> 
(Without dialog window prompt or threading operation to await pair request)
```python
pair_number = 1
pair_confirmation = TrigBase.PairSensor(pair_number)
```

&nbsp;<br>

```C#
public bool CheckPairStatus()
```
After running the PairSensor() command, use this boolean to check if the sensor pair action (i.e. tap to magnet) was completed. Pairing is true while waiting to pair the sensor, and false once the pair has been initiated on a sensor. 

&nbsp;<br>

```C#
public async void CancelPair()
```
Called while a pair is in progress and cancel

&nbsp;<br> 

```C#
public bool SelectAllSensors()
```
Selects all the sensors that have been found in the scan. If you only want to select a specific sensor, use SelectSensor method

&nbsp;<br>  

```C#
public void SelectSensor(int sensorNum)
```
Selects the sensor for streaming at index `sensorNum`. Use SelectAllSensors() method to select all scanned sensors.

&nbsp;<br>  
```C#
public SensorTrignoRf GetSensorObject(int sensorNo)
```
Get the sensor object of the sensor at the index sensorNo 

&nbsp;<br>  
```C#
public List<string> GetAllSampleModes()
```
Get all of the sample modes that the sensors are currently set to.

&nbsp;<br>  
```C#
public string GetCurrentSensorMode(int sensorNo)
```
Get the current sensor mode string of the sensor object at index sensorNo.

&nbsp;<br>  

```C#
public void SetSampleMode(int componentNum, string sampleMode)
```
Sets the sample mode for the given sensor. Will set the sensor at index componentNum to the mode given by sampleMode

&nbsp;<br>  
```C#
public string[] GetSensorNames()
```
Return a string array of the names of the current sensors found in scan

&nbsp;<br>  
```C#
public string[] AvailibleSensorModes(int sensorSelected)
```
Return the list of sensor modes available to the sensor at index sensorSelected

&nbsp;<br>  

### Pre Data Collection Configuration

```C#
public void Configure(bool starttrigger = false, bool stoptrigger = false)
```
Configure pipeline for raw data output on all connected sensors. To enable triggering (start/stop) pass two 'True' booleans to this method. If no arguments are provided, the system will be set up without start/stop triggering enabled. Pipeline will transition to Armed

&nbsp;<br>  


```C#
public bool IsPipelineConfigured()
```
Returns true if the DelsysAPI Pipeline is currently configured for data streaming (ready for Start).
&nbsp;<br>  

### Data Collection Management
By default, this application will stream data from all channels based on what sensor(s) is/are connected (previously paired & scanned in) along with the mode the sensor(s) is/are operating in (See SetSampleMode above). 
Certain sensor modes will have more or less channels than others. See console output after pressing Start to see full list of sensors and their channels.

**Channel GUIDs**

Each Trigno channel will have a unique GUID associated with it. These GUIDs are primarily used when parsing the real-time data packets from the DelsysAPI.
See PollData() definitions below for details. 

Channel GUIDs can be obtained after Configure() and prior to data streaming (Start) so that users have the ability to choose which channels to take during data streaming.
See ConfigureCollectionOutput() method in TrignoBase.py for implementation example.

&nbsp;<br>  

```C#
public void Start(bool ytdata = false)
```
Starts Data Stream - Pipeline must be in the Armed state. Pipeline will transition to Running. Pass 'True' to Start command to get YT data output (use CheckYTDataReady() & PollYTData() )

&nbsp;<br>  
```C#
public bool CheckDataQueue()
```
Called while in the Running state (live data collection) Returns true if there is new data in the internal data buffer that is ready to be extracted. If true, use `PollData()` to return the data.

&nbsp;<br>  

```C#
public bool CheckYTDataQueue()
```
Called while in the Running state (live data collection) Returns true if there is new yt data in the internal data buffer that is ready to be extracted. If true, use `PollYTData()` to return the data.

&nbsp;<br>  

```C#
public Dictionary<Guid, List<double>> PollData()
```
This retrieves the data from the data buffer after the `Start()` method is called. Every time this method is called it will return the data, then clear the internal data queue. The return type is a dictionary output where channel GUID is the key and the channel data is the value

&nbsp;<br>  

```C#
public Dictionary<Guid, List<(double, double)>> PollYTData()
```
This retrieves the data from the data buffer after the `Start(True)` method is called. Every time this method is called it will return the data, then clear the internal data queue. The return type is a dictionary output where channel GUID is the key and the channel data is the value

&nbsp;<br>  

```C#
public void Stop()
```
Stops Data Stream - Pipeline must be in the Running state. Pipeline will transition to Armed

&nbsp;<br>  
```C#
public void ResetPipeline()
```
Resets (disarms) Pipeline - Pipeline must be in the Armed state. Pipeline will transition to Connected (Allows for users to call Scan/Pair after a collections is stopped)

&nbsp;<br>  

```C#
public bool IsWaitingForStartTrigger()
```
If start trigger is enabled (see Configure method above), once the Start() command is initiated this method will return true until the start trigger is pressed, then this method will return false and data streaming will begin.

&nbsp;<br> 

```C#
public bool IsWaitingForStopTrigger()
```
If stop trigger is enabled, once the data collection has started this method will return true until the stop trigger is pressed, then this method will return false and the data streaming will end.

&nbsp;<br> 
### Helper Functions

```C#
public string GetPipelineState()
```
Returns the current state of the RF pipeline

&nbsp;<br>  
```C#
public int GetTotalPackets()
```
Returns the total number of data packets collected from the current streaming session.

```C#
public string GetAPIUnitsEnumString(int enumInt)
```
Returns channel unit string based on unit int value from ChannelTrigno Unit enum

&nbsp;<br>  
```C#
public int GetAPIChannelTypeEnumString(int enumInt)
```
Returns channel type string based on type int value from ChannelTrigno Type enum


&nbsp;<br>

## DelsysAPI Object Properties

### SensorTrignoRF (READ-ONLY)
via GetSensorObject(int sensorNo)
&nbsp;<br>
&nbsp;<br>
```C#
public List<ChannelTrigno> TrignoChannels
```
List if all ChannelTrigno objects associated with the sensor (Channels and properties dependent on the mode the sensor is set to). All EMG modes will have the EMG channel at index 0.
&nbsp;<br>
&nbsp;<br>
```C#
public int PairNumber
```
Number provided by the user on pair.
&nbsp;<br>
&nbsp;<br>

```C#
public string Configuration.ModeString
```
String description of current operating mode
&nbsp;<br>
&nbsp;<br>

```C#
public string[] Configuration.SampleModes
```
List of all available sample modes for the sensor (different sensor types will have different available modes)
&nbsp;<br>
&nbsp;<br>
```C#
public int Properties.Sid
```
Unique SID of the physical sensor. This ID never changes for this sensor.
&nbsp;<br>
&nbsp;<br>

### ChannelTrigno (READ-ONLY)
Channel object via SensorTrignoRF's TrignoChannels list
&nbsp;<br>
&nbsp;<br>

```C#
public Guid Id
```
Channel ID used when parsing real-time data packets from DelsysAPI
&nbsp;<br>
&nbsp;<br>

```C#
public string Name
```
The channel name, typically the type and index. Ex: EMG 1, ACC X etc.
&nbsp;<br>
&nbsp;<br>

```C#
public double SampleRate
```
Sampling frequency of the channel
&nbsp;<br>
&nbsp;<br>

```C#
public Units Unit
```
Channel Unit enum. Use str() in python to get the string representation for this enum. Ex: Millivolts, G, Deg_S etc.
&nbsp;<br>
&nbsp;<br>

```C#
public ChannelTypes Type
```
Channel Type enum. Use str() in python to get the string representation for this enum. Ex: EMG, ACC, GYRO etc.
&nbsp;<br>
&nbsp;<br>

```C#
public bool IsEnabled
```
Certain Trigno channels exist during data streaming that have no use for the user. Channels that are used will have IsEnabled set to True
&nbsp;<br>
&nbsp;<br>