
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

        if self.controller:  # Don't run if just testing UI

            # Update correct image folder dir
            self.el_flex_image.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            self.el_flex_image_2.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            self.el_flex_image_4.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            self.el_flex_image_5.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            self.el_flex_image_9.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            self.el_flex_image_10.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            self.el_flex_image_11.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            self.el_flex_image_12.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))

            # Set button functionalities
            self.el_flex_reset_pushButton.clicked.connect(self.reset_el_flex_max_buttonCallback)
            self.el_ext_reset_pushButton.clicked.connect(self.reset_el_ext_max_buttonCallback)
            self.el_pro_reset_pushButton.clicked.connect(self.reset_el_pro_max_buttonCallback)
            self.el_sup_reset_pushButton.clicked.connect(self.reset_el_sup_max_buttonCallback)
            self.sh_flex_reset_pushButton.clicked.connect(self.reset_sh_flex_max_buttonCallback)
            self.sh_abd_reset_pushButton.clicked.connect(self.reset_sh_abd_max_buttonCallback)
            self.sh_introt_reset_pushButton.clicked.connect(self.reset_sh_introt_max_buttonCallback)
            self.sh_extrot_reset_pushButton.clicked.connect(self.reset_sh_extrot_max_buttonCallback)

            # Create a timer to update the display
            self.update_timer = QTimer()
            self.update_timer.timeout.connect(self.update_display)
            self.update_timer.start(100)  # Update every 100ms

    # -----------------------------------------------------------------------
    # ---- Callback Functions

    def update_display(self):
        if hasattr(self.controller.collectWindow.CallbackConnector, 'el_FE'):
            # Update flexion value and max value
            self.el_flex_value.setText(f"{self.controller.collectWindow.CallbackConnector.el_FE:.0f}°")
            self.el_flex_max_value.setText(f"{self.controller.collectWindow.CallbackConnector.el_flex_max:.0f}°")
            # Update extension value and max value
            self.el_ext_value.setText(f"{self.controller.collectWindow.CallbackConnector.el_FE:.0f}°")
            self.el_ext_max_value.setText(f"{self.controller.collectWindow.CallbackConnector.el_ext_max:.0f}°")

        if hasattr(self.controller.collectWindow.CallbackConnector, 'el_PS'):
            # Update pronation value and max value
            self.el_pro_value.setText(f"{self.controller.collectWindow.CallbackConnector.el_PS:.0f}°")
            self.el_pro_max_value.setText(f"{self.controller.collectWindow.CallbackConnector.el_pro_max:.0f}°")
            # Update supination value and max value
            self.el_sup_value.setText(f"{self.controller.collectWindow.CallbackConnector.el_PS:.0f}°")
            self.el_sup_max_value.setText(f"{self.controller.collectWindow.CallbackConnector.el_sup_max:.0f}°")

        if hasattr(self.controller.collectWindow.CallbackConnector, 'sh_FE'):
            # Update shoulder flexion value and max value
            self.sh_flex_value.setText(f"{self.controller.collectWindow.CallbackConnector.sh_FE:.0f}°")
            self.sh_flex_max_value.setText(f"{self.controller.collectWindow.CallbackConnector.sh_flex_max:.0f}°")

        if hasattr(self.controller.collectWindow.CallbackConnector, 'sh_AB'):
            # Update shoulder abduction value and max value
            self.sh_abd_value.setText(f"{self.controller.collectWindow.CallbackConnector.sh_AB:.0f}°")
            self.sh_abd_max_value.setText(f"{self.controller.collectWindow.CallbackConnector.sh_abd_max:.0f}°")

        if hasattr(self.controller.collectWindow.CallbackConnector, 'sh_IE'):
            # Update shoulder internal rotation value and max value
            self.sh_introt_value.setText(f"{self.controller.collectWindow.CallbackConnector.sh_IE:.0f}°")
            self.sh_introt_max_value.setText(f"{self.controller.collectWindow.CallbackConnector.sh_introt_max:.0f}°")
            # Update shoulder external rotation value and max value
            self.sh_extrot_value.setText(f"{self.controller.collectWindow.CallbackConnector.sh_IE:.0f}°")
            self.sh_extrot_max_value.setText(f"{self.controller.collectWindow.CallbackConnector.sh_extrot_max:.0f}°")


    def closeEvent(self, event):
        if self.controller:
            self.controller.collectWindow.CallbackConnector.vis_dataFlag = False
            self.controller.collectWindow.start_vis_button.setEnabled(True)
            self.controller.collectWindow.start_vis_button.setStyleSheet("color : white")
        event.accept()  # Allow the window to close

    # --- Reset button callbacks

        """ When reset buttons are clicked, Max value is set to current value of that joint angle"""
    def reset_el_flex_max_buttonCallback(self):
        if hasattr(self.controller.collectWindow.CallbackConnector, 'el_FE'):
            self.controller.collectWindow.CallbackConnector.el_flex_max = self.controller.collectWindow.CallbackConnector.el_FE

    def reset_el_ext_max_buttonCallback(self):
        if hasattr(self.controller.collectWindow.CallbackConnector, 'el_FE'):
            self.controller.collectWindow.CallbackConnector.el_ext_max = self.controller.collectWindow.CallbackConnector.el_FE

    def reset_el_pro_max_buttonCallback(self):
        if hasattr(self.controller.collectWindow.CallbackConnector, 'el_PS'):
            self.controller.collectWindow.CallbackConnector.el_pro_max = self.controller.collectWindow.CallbackConnector.el_PS

    def reset_el_sup_max_buttonCallback(self):
        if hasattr(self.controller.collectWindow.CallbackConnector, 'el_PS'):
            self.controller.collectWindow.CallbackConnector.el_sup_max = self.controller.collectWindow.CallbackConnector.el_PS

    def reset_sh_flex_max_buttonCallback(self):
        if hasattr(self.controller.collectWindow.CallbackConnector, 'sh_FE'):
            self.controller.collectWindow.CallbackConnector.sh_flex_max = self.controller.collectWindow.CallbackConnector.sh_FE

    def reset_sh_abd_max_buttonCallback(self):
        if hasattr(self.controller.collectWindow.CallbackConnector, 'sh_AB'):
            self.controller.collectWindow.CallbackConnector.sh_abd_max = self.controller.collectWindow.CallbackConnector.sh_AB

    def reset_sh_introt_max_buttonCallback(self):
        if hasattr(self.controller.collectWindow.CallbackConnector, 'sh_IE'):
            self.controller.collectWindow.CallbackConnector.sh_introt_max = self.controller.collectWindow.CallbackConnector.sh_IE

    def reset_sh_extrot_max_buttonCallback(self):
        if hasattr(self.controller.collectWindow.CallbackConnector, 'sh_IE'):
            self.controller.collectWindow.CallbackConnector.sh_extrot_max = self.controller.collectWindow.CallbackConnector.sh_IE

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = DataVisWindow(None)
    window.show()

    sys.exit(app.exec())