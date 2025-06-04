import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from DataCollector.CollectDataController import *
from DataCollector.CollectionMetricsManagement import CollectionMetricsManagement
from Plotter import GenericPlot as gp


class LiveDataWindow(QWidget):

    def __init__(self, controller):
        QWidget.__init__(self)
        self.controller = controller
        self.grid = QGridLayout()
        self.setStyleSheet("background-color:#3d4c51;")
        self.setWindowTitle("Start Menu")

        imageBox = QVBoxLayout()
        self.im = QPixmap("./Images/delsys.png")
        self.label = QLabel()
        self.label.setPixmap(self.im)
        self.label.setAlignment(Qt.AlignCenter)
        imageBox.addWidget(self.label)
        imageBox.setAlignment(Qt.AlignBaseline)
        imageBox.setContentsMargins(0,100,0,0)
        self.grid.addLayout(imageBox, 0, 0)

        errorbox = QHBoxLayout()
        errorbox.setSpacing(0)
        self.error = QLabel()
        self.error.setText("")
        self.error.setAlignment(Qt.AlignHCenter)
        self.error.setStyleSheet('QLabel {color: red;}')
        errorbox.addWidget(self.error)
        errorbox.setAlignment(Qt.AlignRight)
        self.grid.addLayout(errorbox,1,0)



        self.setLayout(self.grid)
        self.setFixedSize(self.width(), self.height())

        self.plotPanel = self.Plotter()     # Add plot panel
        self.grid.addWidget(self.plotPanel, 0, 2)

        self.MetricsConnector = CollectionMetricsManagement()   # Set the metrics connector
        self.CallbackConnector = PlottingManagement(self, self.MetricsConnector, self.plotCanvas)   # Set the callback connector

    def Plotter(self):
        # TODO: Make blank plot canvas to pass in to PlottingManagement
        widget = QWidget()
        widget.setLayout(QVBoxLayout())

        plot_mode = 'windowed'  # Select between 'scrolling' and 'windowed'
        pc = gp.GenericPlot(plot_mode)
        pc.native.objectName = 'vispyCanvas'
        pc.native.parent = self
        label = QLabel("*This Demo plots EMG Channels only")
        label.setStyleSheet('.QLabel { font-size: 8pt;}')
        label.setFixedHeight(20)
        label.setAlignment(Qt.AlignmentFlag.AlignRight)
        widget.layout().addWidget(pc.native)
        widget.layout().addWidget(label)
        self.plotCanvas = pc

        return widget

    def Do_Nothing_Callback(self):

        print('This button does nothing')


    def closeEvent(self, event):

        event.accept()  # Allow the window to close
        self.controller.closeLiveData()

