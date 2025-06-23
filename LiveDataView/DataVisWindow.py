
import sys
from PySide6.QtWidgets import *

from LiveDataView.live_data_widget1 import Ui_LiveWindow

class TestWindow(QWidget, Ui_LiveWindow):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        # self.setWindowTitle("Test Live Window")


    def closeEvent(self, event):
        self.controller.collectWindow.CallbackConnector.vis_data = False
        self.controller.collectWindow.start_vis_button.setEnabled(True)
        self.controller.collectWindow.start_vis_button.setStyleSheet("color : white")
        event.accept()  # Allow the window to close

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TestWindow()
    window.show()

    sys.exit(app.exec())