import sys
import time
from PySide6.QtWidgets import QWidget, QApplication, QLabel
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt
from os.path import join
import qmt


from LiveDataView.calibration_widget import Ui_calibrationWindow

class CalibrationWindow(QWidget, Ui_calibrationWindow):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.image_folder = r"C:\Users\r03mm22\Documents\GUI Dev\Delsys Python Example\Images"
        run_processes_flag = True

        # Resize to fill screen
        screen = QApplication.primaryScreen().geometry()
        width = int(screen.width() * 0.99)
        height = int(screen.height() * 0.9)
        self.setGeometry(0, 0, width, height)

        self.controller = controller
        self.connector = self.controller.collectWindow.CallbackConnector

        self.calmove_startButton.setEnabled(False)
        self.finishButton.setEnabled(False)

        # Set callback functions
        self.calposeButton.clicked.connect(self.calposeButtonCallback)
        self.calmove_startButton.clicked.connect(self.calmove_startButtonCallback)
        self.finishButton.clicked.connect(self.close)  # Direct connection to close method

        # Add image into Step 1 groupbox
        groupBox = self.step1_groupBox
        layout = groupBox.layout()
        pixmap = QPixmap(join(self.image_folder, 'attachment.png'))

        widget = QLabel()
        widget.setScaledContents(True)  # Optional: scales pixmap to fit label
        widget.setPixmap(pixmap)
        layout.insertWidget(1, widget)
        widget.setFixedSize(375, 312)


        # Update style of progress bars
        progress_bar_style = """
            QProgressBar {
                border: 2px solid black;
                border-radius: 1px;
                background-color: rgb(230, 230, 230);
            }
            QProgressBar::chunk {
                background-color: rgb(0, 120, 215);
                border-radius: 1px;
            }
        """
        self.elbow_progressBar.setValue(0)
        self.wrist_progressBar.setValue(0)
        self.elbow_progressBar.setTextVisible(False)
        self.wrist_progressBar.setTextVisible(False)
        self.elbow_progressBar.setStyleSheet(progress_bar_style)
        self.wrist_progressBar.setStyleSheet(progress_bar_style)

    def showEvent(self, event):
        super().showEvent(event)  # Call the parent class's showEvent
        self.run_process_flag = True
        self.elbow_progressBar.setValue(0)
        self.wrist_progressBar.setValue(0)
        print('Running SubjectSetupWindow showEvent')

    def getJointValue(self, joint_name):
        if hasattr(self.connector, joint_name):
            joint_value = getattr(self.connector, joint_name)
        else:
            joint_value = None

        return joint_value


    def calposeButtonCallback(self):
        self.pose_statusMessage.setText("Done!")
        self.calmove_startButton.setEnabled(True)
        self.elbow_progressBar.setValue(0)
        self.wrist_progressBar.setValue(0)

        self.connector.calibrationCallback()
        self.controller.liveWindow.reset_all_max_values()


    def calmove_startButtonCallback(self):
        self.calmove_startButton.setEnabled(False)

        # Start tracking both movements
        FE_complete = self.track_FE_movement()
        PS_complete = self.track_PS_movement()

        if FE_complete and PS_complete:
            # Ensure both progress bars are at 100%
            self.elbow_progressBar.setValue(100)
            self.wrist_progressBar.setValue(100)

        self.move_statusMessage.setText("Done!")
        self.finishButton.setEnabled(True)


    def track_FE_movement(self):
        self.elbow_progressBar.setValue(0)
        FE_range = 0
        FE_target_range = 400
        FE_prev = self.getJointValue('el_FE')

        while self.run_process_flag and FE_range < FE_target_range: # This should mean the while loop exits when window is closed
            FE_new = self.getJointValue('el_FE')

            if FE_prev is not None and FE_new is not None:
                FE_diff = abs(FE_new - FE_prev)
                if FE_diff > 1:
                    FE_range = min(FE_range + FE_diff, FE_target_range)
                    FE_progress = min((FE_range / FE_target_range) * 100, 100)
                    self.elbow_progressBar.setValue(int(FE_progress))

                FE_prev = FE_new

            QApplication.processEvents()
            time.sleep(0.05)
        print('Exited while loop')

        self.elbow_progressBar.setValue(100)
        return True

    def track_PS_movement(self):
        self.wrist_progressBar.setValue(0)
        PS_range = 0
        PS_target_range = 500
        PS_prev = self.getJointValue('el_PS')

        while self.run_process_flag and PS_range < PS_target_range:
            PS_new = self.getJointValue('el_PS')

            if PS_prev is not None and PS_new is not None:
                PS_diff = abs(PS_new - PS_prev)
                if PS_diff > 2:
                    PS_range = min(PS_range + PS_diff, PS_target_range)
                    PS_progress = min((PS_range / PS_target_range) * 100, 100)
                    self.wrist_progressBar.setValue(int(PS_progress))

                PS_prev = PS_new

            QApplication.processEvents()
            time.sleep(0.05)

        self.wrist_progressBar.setValue(100)
        return True



    def closeEvent(self, event):
        # Reset the button and message states
        self.pose_statusMessage.setText("")
        self.move_statusMessage.setText("")

        self.calmove_startButton.setEnabled(False)
        self.elbow_progressBar.setValue(0)
        self.wrist_progressBar.setValue(0)
        self.finishButton.setEnabled(False)
        self.controller.liveWindow.reset_all_max_values()
        self.run_process_flag = False

        print("closeEvent triggered")
        event.accept()  # Allow the window to close


if __name__ == "__main__":
    controller = None
    app = QApplication(sys.argv)
    window = CalibrationWindow(controller)
    window.show()
    sys.exit(app.exec())
