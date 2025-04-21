
from pythonnet import load

from Export.CsvWriter import CsvWriter

load("coreclr")
import clr
import csv

clr.AddReference("resources\DelsysAPI")
clr.AddReference("System.Collections")


from Aero import AeroPy

# Create an instance
trigno = AeroPy()

# # List all methods
# methods = [method for method in dir(trigno) if not method.startswith('__')]
# for method in methods:
#     print(method)

# # Get help on the object
# help(trigno.AvailibleSensorModes)

# Let's try to get the modes for a sensor (let's say sensor index 0)
try:
    modes = trigno.AvailibleSensorModes(0)
    print("Available modes:", modes)
except Exception as e:
    print("Error:", e)

# You can also check the type of the return value
print("Return type:", type(modes))

# Test change