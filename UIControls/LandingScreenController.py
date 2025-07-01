from DataCollector.CollectWindow import CollectWindow
from StartMenu.StartWindow import StartWindow
from LiveDataView.DataVisWindow import DataVisWindow

class LandingScreenController():
    def __init__(self):
        self.startWindow = StartWindow(self)
        self.collectWindow = CollectWindow(self)
        self.liveWindow = DataVisWindow(self)

        self.startWindow.show()

        self.curHeight = 900
        self.curWidth = 1400

    def showStartMenu(self):
        self.collectWindow.close()
        self.startWindow.show()

    def showCollectData(self):
        self.startWindow.close()
        self.collectWindow.plot_enabled = True
        self.collectWindow.connect_callback()
        self.collectWindow.show()
        self.collectWindow.scan_callback()  # Automatically scan for sensors when this window opens

    def showViewLiveData(self):
        self.liveWindow.show()

