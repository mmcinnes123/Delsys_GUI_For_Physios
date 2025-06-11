from DataCollector.CollectDataWindow import CollectDataWindow
from StartMenu.StartWindow import StartWindow
from LiveDataView.LiveDataWindow import LiveDataWindow


class LandingScreenController():
    def __init__(self):
        self.startWindow = StartWindow(self)
        self.liveWindow = LiveDataWindow(self)
        self.collectWindow = CollectDataWindow(self)

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
        self.collectWindow.close()
        self.liveWindow.show()

    def closeLiveData(self):
        self.collectWindow.show()
        self.collectWindow.stop_callback()
