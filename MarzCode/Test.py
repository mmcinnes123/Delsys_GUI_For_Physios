
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

# Get help on the object
help(trigno.StreamData)
#
# # Method 2
# print(trigno.GetDataLog.__doc__)

