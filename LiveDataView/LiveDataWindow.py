import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# from DataCollector.IMUDataController import *
from DataCollector.CollectDataController import *
# from DataCollector.IMUMetricsManagement import IMUMetricsManagement
from DataCollector.CollectionMetricsManagement import CollectionMetricsManagement
from Plotter import GenericPlot as gp
from Plotter.TestPlot import SimplePlot

# TODO: Start creating your own vispy plot in the LiveDataWindow and see if you can update it from IMUDataController.py

class LiveDataWindow(QWidget):

    def __init__(self, controller):
        QWidget.__init__(self)
        print('Created Instance of LiveDataWindow Class! \n')
        self.controller = controller
        self.grid = QGridLayout()
        self.setStyleSheet("background-color:#3d4c51;")
        self.setWindowTitle("Live Window")

        self.setLayout(self.grid)
        self.setFixedSize(self.width(), self.height())

        self.plotPanel = self.Plotter()     # Add plot panel
        self.grid.addWidget(self.plotPanel, 0, 2)

        self.MetricsConnector = CollectionMetricsManagement()   # Set the metrics connector
        # self.CallbackConnector = PlottingManagement(self, self.MetricsConnector, self.plotCanvas)   # Set the callback connector

        self.collectionLabelPanel = self.CollectionLabelPanel()
        self.collectionLabelPanel.setFixedHeight(275)
        self.metricspanel = QWidget()
        self.metricspane = QHBoxLayout()
        self.metricspane.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.metricspane.addWidget(self.collectionLabelPanel)
        self.metricspane.addWidget(self.MetricsConnector.collectionmetrics)
        self.metricspanel.setLayout(self.metricspane)
        self.metricspanel.setFixedWidth(400)
        self.grid.addWidget(self.metricspanel, 0, 1)

    def Plotter(self):
        widget = QWidget()
        widget.setLayout(QVBoxLayout())

        plot_mode = 'windowed'  # Select between 'scrolling' and 'windowed'
        pc = SimplePlot(plot_mode)
        pc.native.objectName = 'vispyCanvas'
        pc.native.parent = self
        label = QLabel("My Live Data Window Plotter")
        label.setStyleSheet('.QLabel { font-size: 8pt;}')
        label.setFixedHeight(20)
        label.setAlignment(Qt.AlignmentFlag.AlignRight)
        widget.layout().addWidget(pc.native)
        widget.layout().addWidget(label)
        self.plotCanvas = pc

        return widget


    def CollectionLabelPanel(self):
        collectionLabelPanel = QWidget()
        collectionlabelsLayout = QVBoxLayout()

        mylabel = QLabel('My Label:', self)
        mylabel.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        mylabel.setStyleSheet("color:white")
        collectionlabelsLayout.addWidget(mylabel)

        collectionLabelPanel.setFixedWidth(200)
        collectionLabelPanel.setLayout(collectionlabelsLayout)

        return collectionLabelPanel

    # def start_callback(self):
    #     self.CallbackConnector.base.Start_Callback(False, False)    # Set start and stop triggers to False because we're not using them
    #     self.CallbackConnector.resetmetrics()

    def closeEvent(self, event):

        event.accept()  # Allow the window to close
        self.controller.closeLiveData()

