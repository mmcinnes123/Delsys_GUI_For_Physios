import sys
from PySide6.QtWidgets import QWidget, QApplication


from LiveDataView.calibration_widget import Ui_calibrationWindow

class CalibrationWindow(QWidget, Ui_calibrationWindow):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller


if __name__ == "__main__":
    controller = None
    app = QApplication(sys.argv)
    window = CalibrationWindow(controller)
    window.show()
    sys.exit(app.exec())
