
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer

from LiveDataView.live_data_widget1 import Ui_LiveWindow

class TestWindow(QWidget, Ui_LiveWindow):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

        # Create a timer to update the display
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_display)
        self.update_timer.start(100)  # Update every 100ms

    def update_display(self):
        if hasattr(self.controller.collectWindow.CallbackConnector, 'senA_euls'):
            self.current_angle.setText(f"{self.controller.collectWindow.CallbackConnector.senA_euls[0]:.1f}°")

        # some_number = 92
        # self.current_angle.setText(f"{some_number:.1f}°")

    def closeEvent(self, event):
        self.controller.collectWindow.CallbackConnector.vis_data = False
        self.controller.collectWindow.start_vis_button.setEnabled(True)
        self.controller.collectWindow.start_vis_button.setStyleSheet("color : white")
        event.accept()  # Allow the window to close

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = TestWindow(None)
    window.show()

    sys.exit(app.exec())