import sys
from PySide6.QtWidgets import QWidget, QApplication


from LiveDataView.calibration_widget import Ui_calibrationWindow

class CalibrationWindow(QWidget, Ui_calibrationWindow):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.calmove_startButton.setEnabled(False)
        self.calmove_endButton.setEnabled(False)

        # Set callback functions
        self.calposeButton.clicked.connect(self.calposeButtonCallback)
        self.calmove_startButton.clicked.connect(self.calmove_startButtonCallback)
        self.calmove_endButton.clicked.connect(self.calmove_endButtonCallback)


    def calposeButtonCallback(self):
        self.pose_statusMessage.setText("Done!")
        self.calposeButton.setEnabled(False)
        self.calmove_startButton.setEnabled(True)

        self.connector = self.controller.collectWindow.CallbackConnector
        self.connector.calibrationCallback()


    def calmove_startButtonCallback(self):
        self.calmove_startButton.setEnabled(False)
        self.calmove_endButton.setEnabled(True)

    def calmove_endButtonCallback(self):
        self.move_statusMessage.setText("Done!")
        self.calmove_endButton.setEnabled(False)





if __name__ == "__main__":
    controller = None
    app = QApplication(sys.argv)
    window = CalibrationWindow(controller)
    window.show()
    sys.exit(app.exec())
