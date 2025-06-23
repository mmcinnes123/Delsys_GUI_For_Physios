"""
Data Collector GUI
This is the GUI that lets you connect to a base, scan via rf for sensors, and stream data from them in real time.
"""

import sys
import threading
import time
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import tkinter as tk
from tkinter import filedialog

from DataCollector.CollectDataController import *
from DataCollector.IMUDataController import *
from DataCollector.CollectionMetricsManagement import CollectionMetricsManagement
from Plotter.TestPlot import SimplePlot

from Plotter import GenericPlot as gp

class CollectDataWindow(QWidget):
    plot_enabled = False

    def __init__(self, controller):
        QWidget.__init__(self)
        self.pipelinetext = "Off"
        self.controller = controller
        self.live_data_window = controller.liveWindow
        self.ConnectMetricsConnector = CollectionMetricsManagement()

        self.buttonPanel = self.ButtonPanel()
        self.plotPanel = self.Plotter()


        self.metricsPanel = self.MetricsPanel()

        self.grid = QGridLayout(self)

        self.grid.addWidget(self.plotPanel, 0, 2)
        self.grid.addWidget(self.buttonPanel, 0, 0)
        self.grid.addWidget(self.metricsPanel, 0, 1)

        self.setStyleSheet("background-color:#3d4c51;")
        self.setLayout(self.grid)
        self.setWindowTitle("Collect Data GUI")
        self.pairing = False
        self.selectedSensor = None

        self.CallbackConnector = IMUPlottingManagement(self.live_data_window, self)


    # -----------------------------------------------------------------------
    # ---- GUI Components

    def ConnectMetricPanel(self):
        self.connectMetricsPanel = QWidget()
        self.connectmetricspane = QHBoxLayout()
        self.connectmetricspane.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.collectionLabelPanel = self.CollectionLabelPanel()
        self.connectmetricspane.addWidget(self.collectionLabelPanel)
        self.connectmetricspane.addWidget(self.ConnectMetricsConnector.collectionmetrics) # Get metrics panel from CollectionMetricsManagement
        self.collectionLabelPanel.setFixedHeight(275)
        self.ConnectMetricsConnector.collectionmetrics.setFixedHeight(275)
        self.connectMetricsPanel.setLayout(self.connectmetricspane)
        self.connectMetricsPanel.setFixedWidth(400)
        return self.connectMetricsPanel

    def MetricsPanel(self):
        self.metricsPanel = QWidget()
        self.metricspane = QVBoxLayout()
        self.connectMetricsPanel = self.ConnectMetricPanel()
        self.testMetricPanel = self.TestMetricsPanel()
        self.metricspane.addWidget(self.connectMetricsPanel)
        self.metricspane.addWidget(self.testMetricPanel)
        self.metricsPanel.setLayout(self.metricspane)
        self.metricsPanel.setFixedWidth(400)
        return self.metricsPanel

    def TestMetricsPanel(self):
        self.testMetricsPanel = QWidget()
        self.testmetricspane = QHBoxLayout()
        self.testmetricspane.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.testLabelPanel = self.TestLabelPanel()
        self.testmetricspane.addWidget(self.testLabelPanel)
        self.testmetricspane.addWidget(self.ConnectMetricsConnector.imuTestValues)
        self.testLabelPanel.setFixedHeight(275)
        self.ConnectMetricsConnector.imuTestValues.setFixedHeight(275)
        self.testMetricsPanel.setLayout(self.testmetricspane)
        self.testMetricsPanel.setFixedWidth(400)
        return self.testMetricsPanel

    def ButtonPanel(self):
        buttonPanel = QWidget()
        buttonPanel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        buttonLayout = QVBoxLayout()
        findSensor_layout = QHBoxLayout()
        # ---- Pair Button
        self.pair_button = QPushButton('Pair', self)
        self.pair_button.setToolTip('Pair Sensors')
        self.pair_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.pair_button.objectName = 'Pair'
        self.pair_button.clicked.connect(self.pair_callback)
        self.pair_button.setStyleSheet('QPushButton {color: grey;}')
        self.pair_button.setEnabled(False)
        self.pair_button.setFixedHeight(50)
        findSensor_layout.addWidget(self.pair_button)

        # ---- Scan Button
        self.scan_button = QPushButton('Scan', self)
        self.scan_button.setToolTip('Scan for Sensors')
        self.scan_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.scan_button.objectName = 'Scan'
        self.scan_button.clicked.connect(self.scan_callback)
        self.scan_button.setStyleSheet('QPushButton {color: grey;}')
        self.scan_button.setEnabled(False)
        self.scan_button.setFixedHeight(50)
        findSensor_layout.addWidget(self.scan_button)

        buttonLayout.addLayout(findSensor_layout)

        # ---- Start Button
        self.start_button = QPushButton('Start', self)
        self.start_button.setToolTip('Start Sensor Stream')
        self.start_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.start_button.objectName = 'Start'
        self.start_button.clicked.connect(self.start_callback)
        self.start_button.setStyleSheet('QPushButton {color: grey;}')
        self.start_button.setEnabled(False)
        self.start_button.setFixedHeight(50)
        buttonLayout.addWidget(self.start_button)

        # ---- Stop Button
        self.stop_button = QPushButton('Stop', self)
        self.stop_button.setToolTip('Stop Sensor Stream')
        self.stop_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.stop_button.objectName = 'Stop'
        self.stop_button.clicked.connect(self.stop_callback)
        self.stop_button.setStyleSheet('QPushButton {color: grey;}')
        self.stop_button.setEnabled(False)
        self.stop_button.setFixedHeight(50)
        buttonLayout.addWidget(self.stop_button)

        # ---- Live Data Window Button
        self.start_vis_button = QPushButton('Start Visualisation', self)
        self.start_vis_button.setToolTip('Show Live Data Window')
        self.start_vis_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.start_vis_button.objectName = 'ShowLive'
        self.start_vis_button.clicked.connect(self.start_vis_callback)
        self.start_vis_button.setStyleSheet('QPushButton {color: grey;}')
        self.start_vis_button.setEnabled(False)
        self.start_vis_button.setFixedHeight(50)
        buttonLayout.addWidget(self.start_vis_button)

        # ---- Export CSV Button
        self.exportcsv_button = QPushButton('Export CSV', self)
        self.exportcsv_button.setToolTip('Export collected data to project root - data.csv')
        self.exportcsv_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.exportcsv_button.objectName = 'Export'
        self.exportcsv_button.clicked.connect(self.exportcsv_callback)
        self.exportcsv_button.setStyleSheet('QPushButton {color: grey;}')
        self.exportcsv_button.setEnabled(False)
        self.exportcsv_button.setFixedHeight(50)
        buttonLayout.addWidget(self.exportcsv_button)

        # # ---- Drop-down menu of sensor modes
        # self.SensorModeList = QComboBox(self)
        # self.SensorModeList.setToolTip('Sensor Modes')
        # self.SensorModeList.objectName = 'PlaceHolder'
        # self.SensorModeList.setStyleSheet('QComboBox {color: white;background: #848482}')
        # buttonLayout.addWidget(self.SensorModeList)

        # ---- List of detected sensors
        self.SensorListBox = QListWidget(self)
        self.SensorListBox.setToolTip('Sensor List')
        self.SensorListBox.objectName = 'PlaceHolder'
        self.SensorListBox.setStyleSheet('QListWidget {color: white;background:#848482}')
        self.SensorListBox.itemClicked.connect(self.sensorMode_callback)
        self.SensorListBox.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        buttonLayout.addWidget(self.SensorListBox)
        buttonPanel.setLayout(buttonLayout)
        buttonPanel.setFixedWidth(275)
        return buttonPanel

    def Plotter(self):
        widget = QWidget()
        widget.setLayout(QVBoxLayout())

        plot_mode = 'windowed'  # Select between 'scrolling' and 'windowed'
        pc = SimplePlot(plot_mode)
        pc.native.objectName = 'vispyCanvas'
        pc.native.parent = self
        label = QLabel("My Test Window Plotter")
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

        pipelinelabel = QLabel('Pipeline State:')
        pipelinelabel.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        pipelinelabel.setStyleSheet("color:white")
        collectionlabelsLayout.addWidget(pipelinelabel)

        sensorsconnectedlabel = QLabel('Sensors Connected:', self)
        sensorsconnectedlabel.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        sensorsconnectedlabel.setStyleSheet("color:white")
        collectionlabelsLayout.addWidget(sensorsconnectedlabel)

        totalchannelslabel = QLabel('Total Channels:', self)
        totalchannelslabel.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        totalchannelslabel.setStyleSheet("color:white")
        collectionlabelsLayout.addWidget(totalchannelslabel)

        framescollectedlabel = QLabel('Frames Collected:', self)
        framescollectedlabel.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        framescollectedlabel.setStyleSheet("color:white")
        collectionlabelsLayout.addWidget(framescollectedlabel)

        collectionLabelPanel.setFixedWidth(200)
        collectionLabelPanel.setLayout(collectionlabelsLayout)

        return collectionLabelPanel

    def TestLabelPanel(self):
        testLabelPanel = QWidget()
        testlabelsLayout = QVBoxLayout()

        senAeul1label = QLabel('Sensor A Yaw:')
        senAeul1label.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        senAeul1label.setStyleSheet("color:white")
        testlabelsLayout.addWidget(senAeul1label)

        senAeul2label = QLabel('Sensor A Roll:')
        senAeul2label.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        senAeul2label.setStyleSheet("color:white")
        testlabelsLayout.addWidget(senAeul2label)

        senAeul3label = QLabel('Sensor A Pitch:')
        senAeul3label.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        senAeul3label.setStyleSheet("color:white")
        testlabelsLayout.addWidget(senAeul3label)

        line1 = QFrame()
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)
        line1.setStyleSheet("background-color: white")
        testlabelsLayout.addWidget(line1)

        senBeul1label = QLabel('Sensor B Yaw:')
        senBeul1label.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        senBeul1label.setStyleSheet("color:white")
        testlabelsLayout.addWidget(senBeul1label)

        senBeul2label = QLabel('Sensor B Roll:')
        senBeul2label.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        senBeul2label.setStyleSheet("color:white")
        testlabelsLayout.addWidget(senBeul2label)

        senBeul3label = QLabel('Sensor B Pitch:')
        senBeul3label.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        senBeul3label.setStyleSheet("color:white")
        testlabelsLayout.addWidget(senBeul3label)

        line1 = QFrame()
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)
        line1.setStyleSheet("background-color: white")
        testlabelsLayout.addWidget(line1)

        senCeul1label = QLabel('Sensor C Yaw:')
        senCeul1label.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        senCeul1label.setStyleSheet("color:white")
        testlabelsLayout.addWidget(senCeul1label)

        senCeul2label = QLabel('Sensor C Roll:')
        senCeul2label.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        senCeul2label.setStyleSheet("color:white")
        testlabelsLayout.addWidget(senCeul2label)

        senCeul3label = QLabel('Sensor C Pitch:')
        senCeul3label.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        senCeul3label.setStyleSheet("color:white")
        testlabelsLayout.addWidget(senCeul3label)

        testLabelPanel.setFixedWidth(200)
        testLabelPanel.setLayout(testlabelsLayout)

        return testLabelPanel

    # -----------------------------------------------------------------------
    # ---- Callback Functions
    def getpipelinestate(self):
        self.pipelinetext = self.CallbackConnector.base.PipelineState_Callback()
        self.ConnectMetricsConnector.pipelinestatelabel.setText(self.pipelinetext)

    def connect_callback(self):
        self.CallbackConnector.base.Connect_Callback()

        self.pair_button.setEnabled(True)
        self.pair_button.setStyleSheet('QPushButton {color: white;}')
        self.scan_button.setEnabled(True)
        self.scan_button.setStyleSheet('QPushButton {color: white;}')
        self.getpipelinestate()
        self.ConnectMetricsConnector.pipelinestatelabel.setText(self.pipelinetext + " (Base Connected)")

    def pair_callback(self):
        """Pair button callback"""
        self.Pair_Window()
        self.getpipelinestate()
        self.exportcsv_button.setEnabled(False)
        self.exportcsv_button.setStyleSheet("color : gray")

    def Pair_Window(self):
        """Open pair sensor window to set pair number and begin pairing process"""
        pair_number, pressed = QInputDialog.getInt(QWidget(), "Input Pair Number", "Pair Number:",
                                                   1, 0, 100, 1)
        if pressed:
            self.pairing = True
            self.pair_canceled = False
            self.CallbackConnector.base.pair_number = pair_number
            self.PairThreadManager()

    def PairThreadManager(self):
        """Start t1 thread to begin pairing operation in DelsysAPI
           Start t2 thread to await result of CheckPairStatus() to return False
           Once threads begin, display awaiting sensor pair request window/countdown"""

        self.t1 = threading.Thread(target=self.CallbackConnector.base.Pair_Callback)
        self.t1.start()

        self.t2 = threading.Thread(target=self.awaitPairThread)
        self.t2.start()

        self.BeginPairingUISequence()


    def BeginPairingUISequence(self):
        """The awaiting sensor window will stay open until either:
           A) The pairing countdown timer completes (The end of the countdown will send a CancelPair request to the DelsysAPI)
           or...
           B) A sensor has been paired to the base (via self.pairing flag set by DelsysAPI CheckPairStatus() bool)

           If a sensor is paired, ask the user if they want to pair another sensor (No = start a scan for all previously paired sensors)
        """

        pair_success = False
        self.pair_countdown_seconds = 15

        awaitingPairWindow = QDialog()
        awaitingPairWindow.setWindowTitle(
            "Sensor (" + str(self.CallbackConnector.base.pair_number) + ") Awaiting sensor pair request. . . Cancel in: " + str(self.pair_countdown_seconds))
        awaitingPairWindow.setFixedWidth(500)
        awaitingPairWindow.setFixedHeight(80)
        awaitingPairWindow.show()

        while self.pair_countdown_seconds > 0:
            if self.pairing:
                time.sleep(1)
                self.pair_countdown_seconds -= 1
                self.UpdateTimerUI(awaitingPairWindow)
            else:
                pair_success = True
                break

        awaitingPairWindow.close()
        if not pair_success:
            self.CallbackConnector.base.TrigBase.CancelPair()
        else:
            self.ShowPairAnotherSensorDialog()

    def awaitPairThread(self):
        """ Wait for a sensor to be paired
        Once PairSensor() command is sent to the DelsysAPI, CheckPairStatus() will return True until a sensor has been paired to the base"""
        time.sleep(1)
        while self.pairing:
            pairstatus = self.CallbackConnector.base.CheckPairStatus()
            if not pairstatus:
                self.pairing = False

    def UpdateTimerUI(self, awaitingPairWindow):
        awaitingPairWindow.setWindowTitle(
            "Sensor (" + str(self.CallbackConnector.base.pair_number) + ") Awaiting sensor pair request. . . Cancel in: " + str(self.pair_countdown_seconds))

    def ShowPairAnotherSensorDialog(self):
        messagebox = QMessageBox()
        messagebox.setText("Pair another sensor?")
        messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        messagebox.setIcon(QMessageBox.Question)
        button = messagebox.exec_()

        if button == QMessageBox.Yes:
            self.Pair_Window()
        else:
            self.scan_callback()

    def scan_callback(self):
        sensorList = self.CallbackConnector.base.Scan_Callback()

        self.set_sensor_list_box(sensorList)

        if len(sensorList) > 0:
            self.start_button.setEnabled(True)
            self.start_button.setStyleSheet("color : white")
            self.ConnectMetricsConnector.sensorsconnected.setText(str(len(sensorList)))
            self.getpipelinestate()
            self.exportcsv_button.setEnabled(False)
            self.exportcsv_button.setStyleSheet("color : gray")

            self.autosetsensorMode_callback()

    def set_sensor_list_box(self, sensorList):
        self.SensorListBox.clear()

        number_and_names_str = []
        for i in range(len(sensorList)):
            number_and_names_str.append("(" + str(sensorList[i].PairNumber) + ") " + sensorList[i].FriendlyName)
            for j in range(len(sensorList[i].TrignoChannels)):
                if sensorList[i].TrignoChannels[j].IsEnabled and not str(sensorList[i].TrignoChannels[j].Type) == "SkinCheck":
                    number_and_names_str[i] += "\n     -" + sensorList[i].TrignoChannels[j].Name + " (" + str(
                        round(sensorList[i].TrignoChannels[j].SampleRate, 3)) + " Hz)"

        self.SensorListBox.addItems(number_and_names_str)

    def start_callback(self):
        self.CallbackConnector.base.Start_Callback(False, False)    # Set start and stop triggers to False because we're not using them
        self.CallbackConnector.resetmetrics()

        self.stop_button.setEnabled(True)
        self.stop_button.setStyleSheet("color : white")
        self.start_vis_button.setEnabled(True)
        self.start_vis_button.setStyleSheet("color : white")
        self.start_button.setEnabled(False)
        self.start_button.setStyleSheet("color : gray")
        self.exportcsv_button.setEnabled(False)
        self.exportcsv_button.setStyleSheet("color : gray")

        self.getpipelinestate()

    def stop_callback(self):
        self.CallbackConnector.base.Stop_Callback()
        self.getpipelinestate()

        self.exportcsv_button.setEnabled(True)
        self.exportcsv_button.setStyleSheet("color : white")
        self.start_button.setEnabled(True)
        self.start_button.setStyleSheet("color : white")
        self.stop_button.setEnabled(False)
        self.stop_button.setStyleSheet("color : gray")
        self.start_vis_button.setEnabled(False)
        self.start_vis_button.setStyleSheet("color : gray")


    def start_vis_callback(self):
        self.start_vis_button.setEnabled(False)
        self.start_vis_button.setStyleSheet("color : gray")
        self.CallbackConnector.vis_data = True
        self.controller.showViewLiveData()  # Open live data view

    def exportcsv_callback(self):
        export = None
        if self.CallbackConnector.streamYTData:
            export = self.CallbackConnector.base.csv_writer.exportYTCSV()
        else:
            export = self.CallbackConnector.base.csv_writer.exportCSV()
        self.getpipelinestate()
        print("CSV Export: " + str(export))

    def sensorMode_callback(self):

        # See original repo to see how this used to work with a drop down of available sensor modes

        # Get the current selected sensor
        current_selected = self.SensorListBox.currentRow()

        # Only implement if the selected sensor has changed
        if self.selectedSensor is None or self.selectedSensor != current_selected:

            self.selectedSensor = self.SensorListBox.currentRow()

            curItem = self.SensorListBox.currentRow()
            selMode = 'EMG RMS x4 (222Hz, 100ms win), OR 20 bits (74Hz), +/-5.5mV, 20-450Hz'
            # self.print_available_sensor_modes()   # To see other modes, use the print_available_sensor_modes function

            # Set the sensor mode
            self.CallbackConnector.base.setSampleMode(curItem, selMode)
            self.getpipelinestate()

            # Verify sensor mode
            curMode = self.CallbackConnector.base.getCurMode(self.selectedSensor)
            print(f"\nMode for sensor #{self.selectedSensor} set to:")
            print('\n   ', curMode)

    def autosetsensorMode_callback(self):

        # Set to this mode which has four EMG channels and 4 Orientation (q_w, q_x, q_y, q_z)
        selMode = 'EMG RMS x4 (222Hz, 100ms win), OR 20 bits (74Hz), +/-5.5mV, 20-450Hz'

        # Iterate through each sensor
        total_sensors = self.SensorListBox.count()
        for sensor_idx in range(total_sensors):

            self.CallbackConnector.base.setSampleMode(sensor_idx, selMode)

            # Verify each sensor's mode
            curMode = self.CallbackConnector.base.getCurMode(sensor_idx)
            print(f"\nMode for sensor #{sensor_idx} set to:")
            print('\n   ', curMode)

        # After setting all sensors, update pipeline state
        self.getpipelinestate()

    def print_available_sensor_modes(self):
        """
        Prints all available sensor modes for the currently selected sensor.
        If no sensor is selected, prints a message indicating that.
        """
        if self.selectedSensor is not None:
            # Get the list of available modes for the selected sensor
            mode_list = self.CallbackConnector.base.getSampleModes(self.selectedSensor)

            # Get the current mode
            current_mode = self.CallbackConnector.base.getCurMode(self.selectedSensor)

            print(f"\nAvailable modes for sensor #{self.selectedSensor}:")
            print("-" * 40)

            # Print each available mode, marking the current mode with an asterisk
            for mode in mode_list:
                if mode == current_mode:
                    print(f"* {mode} (current)")
                else:
                    print(f"  {mode}")
        else:
            print("No sensor selected. Please select a sensor first.")

    def closeEvent(self, event):
        self.getpipelinestate()
        if self.pipelinetext == 'Running':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Pipeline is still running!")
            msg.setInformativeText("Please stop the pipeline before closing.")
            msg.setWindowTitle("Warning")
            msg.exec()
            # Reject the close event
            event.ignore()
        else:
            # Pipeline is not running, accept the close event
            event.accept()

