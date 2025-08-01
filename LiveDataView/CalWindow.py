import sys
from PySide6.QtWidgets import QWidget, QApplication


from LiveDataView.calibration_widget import Ui_calibrationWindow

class CalibrationWindow(QWidget, Ui_calibrationWindow):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)

        # Resize to fill screen
        screen = QApplication.primaryScreen().geometry()
        width = int(screen.width() * 1)
        height = int(screen.height() * 0.9)
        self.setGeometry(0, 0, width, height)

        self.controller = controller
        self.calmove_startButton.setEnabled(False)
        self.calmove_endButton.setEnabled(False)
        self.finishButton.setEnabled(False)

        # Set callback functions
        self.calposeButton.clicked.connect(self.calposeButtonCallback)
        self.calmove_startButton.clicked.connect(self.calmove_startButtonCallback)
        self.calmove_endButton.clicked.connect(self.calmove_endButtonCallback)
        self.finishButton.clicked.connect(self.close)  # Direct connection to close method


    def calposeButtonCallback(self):
        self.pose_statusMessage.setText("Done!")
        self.calmove_startButton.setEnabled(True)

        self.connector = self.controller.collectWindow.CallbackConnector
        self.connector.calibrationCallback()


    def calmove_startButtonCallback(self):
        self.calmove_startButton.setEnabled(False)
        self.calmove_endButton.setEnabled(True)

    def calmove_endButtonCallback(self):
        self.move_statusMessage.setText("Done!")
        self.calmove_endButton.setEnabled(False)
        self.finishButton.setEnabled(True)

    def closeEvent(self, event):
        # Reset the button and message states
        self.pose_statusMessage.setText("")
        self.move_statusMessage.setText("")

        self.calmove_startButton.setEnabled(False)
        self.calmove_endButton.setEnabled(False)
        self.finishButton.setEnabled(False)
        event.accept()  # Allow the window to close


if __name__ == "__main__":
    controller = None
    app = QApplication(sys.argv)
    window = CalibrationWindow(controller)
    window.show()
    sys.exit(app.exec())
