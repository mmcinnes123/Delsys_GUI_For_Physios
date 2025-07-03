
import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap

from LiveDataView.LineAngleWidget import LineAngleWidget
from LiveDataView.live_data_widget1 import Ui_LiveWindow

class DataVisWindow(QWidget, Ui_LiveWindow):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

        self.sh_flex_ani_widget = LineAngleWidget()
        self.gridLayout_12.addWidget(self.sh_flex_ani_widget, 1, 0, 1, 2)
        self.sh_flex_ani_widget.setMinimumSize(200, 100)

        # Update the animated line angle
        angle = 150
        self.sh_flex_ani_widget.set_angle(angle)

        if self.controller:  # Don't run if just testing UI

            # Update correct image folder dir
            self.el_flex_image.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            self.el_flex_image_2.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            self.el_flex_image_4.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            self.el_flex_image_5.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            self.el_flex_image_9.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            self.el_flex_image_10.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
            # self.el_flex_image_11.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
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

        # Define joint mapping: (attribute_name, value_widget, max_value_widget)
        joint_mapping = {
            'el_flex': (self.el_flex_value, self.el_flex_max_value, self.el_flex_groupBox),
            'el_ext': (self.el_ext_value, self.el_ext_max_value, self.el_ext_groupBox),
            'el_pro': (self.el_pro_value, self.el_pro_max_value, self.el_pro_groupBox),
            'el_sup': (self.el_sup_value, self.el_sup_max_value, self.el_sup_groupBox),
            'sh_flex': (self.sh_flex_value, self.sh_flex_max_value, self.sh_flex_groupBox),
            'sh_abd': (self.sh_abd_value, self.sh_abd_max_value, self.sh_abd_groupBox),
            'sh_introt': (self.sh_introt_value, self.sh_introt_max_value, self.sh_introt_groupBox),
            'sh_extrot': (self.sh_extrot_value, self.sh_extrot_max_value, self.sh_extrot_groupBox)
        }

        connector = self.controller.collectWindow.CallbackConnector

        for joint_name, (value_widget, max_widget, groupbox) in joint_mapping.items():
            if hasattr(connector, joint_name):
                joint_value = getattr(connector, joint_name)
                max_value = getattr(connector, f"{joint_name}_max")

                if joint_value is not None:
                    value_widget.setText(f"{joint_value:.0f}°")
                    self.toggle_groupbox_state(groupbox, True)  # Enable groupbox
                else:
                    value_widget.setText("-°")
                    self.toggle_groupbox_state(groupbox, False)  # Disable groupbox

                if max_value is not None:
                    max_widget.setText(f"{max_value:.0f}°")
                else:
                    max_widget.setText("-°")


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


    def toggle_groupbox_state(self, groupbox, enabled=True):

        if enabled:
            # Reset to default style (black text)
            groupbox.setStyleSheet("")
        else:
            # Grey out the text
            groupbox.setStyleSheet("""
                QGroupBox * {
                    color: gray;
                }
                QGroupBox::title {
                    color: gray;
                }
            """)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = DataVisWindow(None)
    window.show()

    sys.exit(app.exec())