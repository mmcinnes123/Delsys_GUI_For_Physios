from DataCollector.ConnectWindow import ConnectWindow
from StartMenu.StartWindow import StartWindow
from LiveDataView.DataVisWindow import DataVisWindow
from LiveDataView.CalWindow import CalibrationWindow
from LiveDataView.CompassCalWindow import CompassCalibrationWindow

class LandingScreenController():

    def __init__(self):

        # Create instances of each app window, passing itself (the controller) as an argument
        self.startWindow = StartWindow(self)
        self.connectWindow = ConnectWindow(self)
        self.liveWindow = DataVisWindow(self)
        self.calWindow = CalibrationWindow(self)
        self.compasscalWindow = CompassCalibrationWindow(self)

        # Open the start window
        self.startWindow.show()
        self.curHeight = 900
        self.curWidth = 1400

    def showStartMenu(self):
        self.connectWindow.close()
        self.startWindow.show()

    def showConnectWindow(self):
        self.startWindow.close()
        self.connectWindow.connect_callback()
        self.connectWindow.show()
        self.connectWindow.scan_callback()  # Automatically scan for sensors when this window opens

    def showViewLiveData(self):
        self.liveWindow.show()
        self.calWindow.show()
        self.compasscalWindow.show()
        self.compasscalWindow._running = True
        self.compasscalWindow.reset_buttonCallback()
        self.compasscalWindow.compasscal_Callback()

