import sys
import time
from PySide6.QtWidgets import QWidget, QApplication, QLabel
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt
from os.path import join
import qmt


from LiveDataView.compass_cal_widget import Ui_CompassCalibration

class CompassCalibrationWindow(QWidget, Ui_CompassCalibration):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.image_folder = r"C:\Users\r03mm22\Documents\GUI Dev\Delsys Python Example\Images"

        # Resize to fill screen
        screen = QApplication.primaryScreen().geometry()
        width = int(screen.width() * 1)
        height = int(screen.height() * 0.8)
        self.setGeometry(0, 0, width, height)

        self.controller = controller
        self.connector = self.controller.collectWindow.CallbackConnector
        self.finishButton.setEnabled(False)
        self.finishButton.clicked.connect(self.close)  # Direct connection to close method


    def compasscal_Callback(self):

        # Start tracking both movements
        sen1_complete = self.track_sensor_movement('1')
        sen2_complete = self.track_sensor_movement('2')
        sen3_complete = self.track_sensor_movement('3')

        if sen1_complete and sen2_complete and sen3_complete:

            # Ensure both progress bars are at 100%
            self.sensor1_progressBar.setValue(100)
            self.sensor2_progressBar.setValue(100)
            self.sensor3_progressBar.setValue(100)

        self.finishButton.setEnabled(True)

    def track_sensor_movement(self, senNo):

        if senNo == '1':
            quat_att = 'sen1_quat'
            progress_bar = self.sensor1_progressBar
            progress_label = self.sensor1_progressLabel
        elif senNo == '2':
            quat_att = 'sen2_quat'
            progress_bar = self.sensor2_progressBar
            progress_label = self.sensor2_progressLabel
        else:
            quat_att = 'sen3_quat'
            progress_bar = self.sensor3_progressBar
            progress_label = self.sensor3_progressLabel

        # Get initial state
        sen_prev = getattr(self.connector, quat_att)

        target_range = 20
        sen_range = 0
        while sen_range < target_range:

            # Get change in orientation as a single angle
            sen_new = getattr(self.connector, quat_att)
            rot = qmt.qrel(sen_new, sen_prev)
            angle_diff = qmt.quatAngle(rot)
            sen_range = sen_range + angle_diff

            # Set progress bar value
            progress_bar.setValue((sen_range / target_range) * 100)

            sen_prev = sen_new

            QApplication.processEvents()
            time.sleep(0.1)

        progress_bar.setValue(100)
        progress_label.setText("Done!")


        return True

    def closeEvent(self, event):
        # Reset the button and message states
        self.sensor1_progressLabel.setText("")
        self.sensor2_progressLabel.setText("")
        self.sensor3_progressLabel.setText("")

        self.finishButton.setEnabled(False)

        event.accept()  # Allow the window to close