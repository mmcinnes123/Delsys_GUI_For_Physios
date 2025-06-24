
import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap

from LiveDataView.live_data_widget1 import Ui_LiveWindow

class DataVisWindow(QWidget, Ui_LiveWindow):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

        # Set button functionalities
        self.el_flex_reset_pushButton.clicked.connect(self.reset_el_flex_max_buttonCallback)

        # Update correct image folder dir
        self.el_flex_image.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))


        # Create a timer to update the display
        if self.controller:  # Don't run if just testing UI
            self.update_timer = QTimer()
            self.update_timer.timeout.connect(self.update_display)
            self.update_timer.start(100)  # Update every 100ms

    # -----------------------------------------------------------------------
    # ---- Callback Functions

    def update_display(self):
        if hasattr(self.controller.connectWindow.CallbackConnector, 'senA_euls'):
            self.el_flex_value.setText(f"{self.controller.connectWindow.CallbackConnector.senA_euls[0]:.0f}°")
            self.el_flex_max_value.setText(f"{self.controller.connectWindow.CallbackConnector.senA_eul1_max:.0f}°")

    def reset_el_flex_max_buttonCallback(self):
        if hasattr(self.controller.connectWindow.CallbackConnector, 'senA_eul1_max'):
            self.controller.connectWindow.CallbackConnector.senA_eul1_max = 0

    def closeEvent(self, event):
        if self.controller:
            self.controller.connectWindow.CallbackConnector.vis_data = False
            self.controller.connectWindow.start_vis_button.setEnabled(True)
            self.controller.connectWindow.start_vis_button.setStyleSheet("color : white")
        event.accept()  # Allow the window to close



if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = DataVisWindow(None)
    window.show()

    sys.exit(app.exec())