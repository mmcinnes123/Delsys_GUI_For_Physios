from DataCollector.ConnectWindow import ConnectWindow
from StartMenu.StartWindow import StartWindow
from LiveDataView.DataVisWindow import DataVisWindow

class LandingScreenController():
    def __init__(self):
        self.startWindow = StartWindow(self)
        # self.liveWindow = LiveDataWindow(self)
        self.liveWindow = DataVisWindow(self)
        self.connectWindow = ConnectWindow(self)

        self.startWindow.show()

        self.curHeight = 900
        self.curWidth = 1400

    def showStartMenu(self):
        self.connectWindow.close()
        self.startWindow.show()

    def showCollectData(self):
        self.startWindow.close()
        self.connectWindow.plot_enabled = True
        self.connectWindow.connect_callback()
        self.connectWindow.show()
        self.connectWindow.scan_callback()  # Automatically scan for sensors when this window opens

    def showViewLiveData(self):
        self.liveWindow.show()

