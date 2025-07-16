
import sys
from os.path import join

from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


from LiveDataView.LineAngleWidget import LineAngleWidget
from LiveDataView.live_data_widget1 import Ui_LiveWindow

class DataVisWindow(QWidget, Ui_LiveWindow):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.image_folder = r"C:\Users\r03mm22\Documents\GUI Dev\Delsys Python Example\Images"

        # Add image and line widget to each groupBox
        self.setup_joint_animations()

        if self.controller:  # Don't run if just testing UI

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
            'el_flex': (self.el_flex_value, self.el_flex_max_value, self.el_flex_groupBox, self.el_flex_ani_widget),
            'el_ext': (self.el_ext_value, self.el_ext_max_value, self.el_ext_groupBox, self.el_ext_ani_widget),
            'el_pro': (self.el_pro_value, self.el_pro_max_value, self.el_pro_groupBox, self.el_pro_ani_widget),
            'el_sup': (self.el_sup_value, self.el_sup_max_value, self.el_sup_groupBox, self.el_sup_ani_widget),
            'sh_flex': (self.sh_flex_value, self.sh_flex_max_value, self.sh_flex_groupBox, self.sh_flex_ani_widget),
            'sh_abd': (self.sh_abd_value, self.sh_abd_max_value, self.sh_abd_groupBox, self.sh_abd_ani_widget),
            'sh_introt': (self.sh_introt_value, self.sh_introt_max_value, self.sh_introt_groupBox,
                          self.sh_introt_ani_widget),
            'sh_extrot': (self.sh_extrot_value, self.sh_extrot_max_value, self.sh_extrot_groupBox,
                          self.sh_extrot_ani_widget)
        }

        connector = self.controller.collectWindow.CallbackConnector

        for joint_name, (value_widget, max_widget, groupbox, ani_widget) in joint_mapping.items():
            if hasattr(connector, joint_name):
                joint_value = getattr(connector, joint_name)
                max_value = getattr(connector, f"{joint_name}_max")

                if joint_value is not None:
                    value_widget.setText(f"{joint_value:.0f}°")
                    self.toggle_groupbox_state(groupbox, True)  # Enable groupbox
                    ani_widget.set_angle(joint_value)  # Update the animation angle
                else:
                    value_widget.setText("-°")
                    self.toggle_groupbox_state(groupbox, False)  # Disable groupbox
                    ani_widget.set_angle(0)  # Reset animation to 0 when no value

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

    # --- Other functions

    def setup_joint_animations(self):
        """
        Sets up animation widgets for all joint angles by adding LineAngleWidgets
        to their respective groupBoxes.
        """
        # Dictionary mapping groupBox attributes to their corresponding image files and anchor positions
        joint_mappings = {
            'sh_flex_groupBox': {
                'image': "GUI_el_flex.png",
                'anchor_x': 0.3,
                'anchor_y': 0.5,
                'line_length': 0.3
            },
            'sh_abd_groupBox': {
                'image': "GUI_el_flex.png",
                'anchor_x': 0.4,
                'anchor_y': 0.6,
                'line_length': 0.25
            },
            'sh_introt_groupBox': {
                'image': "GUI_el_flex.png",
                'anchor_x': 0.5,
                'anchor_y': 0.5,
                'line_length': 0.2
            },
            'sh_extrot_groupBox': {
                'image': "GUI_el_flex.png",
                'anchor_x': 0.5,
                'anchor_y': 0.5,
                'line_length': 0.2
            },
            'el_flex_groupBox': {
                'image': "el_flex_image.png",
                'anchor_x': 0.34,
                'anchor_y': 0.62,
                'line_length': 0.35
            },
            'el_ext_groupBox': {
                'image': "GUI_el_flex.png",
                'anchor_x': 0.5,
                'anchor_y': 0.5,
                'line_length': 0.2
            },
            'el_pro_groupBox': {
                'image': "GUI_el_flex.png",
                'anchor_x': 0.5,
                'anchor_y': 0.5,
                'line_length': 0.2
            },
            'el_sup_groupBox': {
                'image': "GUI_el_flex.png",
                'anchor_x': 0.5,
                'anchor_y': 0.5,
                'line_length': 0.2
            }
        }

        # Add image and line widget to each groupBox
        for groupBox_name, config in joint_mappings.items():

            # Get the groupBox object
            groupBox = getattr(self, groupBox_name)

            # Get the pre-existing layout
            layout = groupBox.layout()

            # Create widget name (remove '_groupBox' and add '_ani_widget')
            widget_name = groupBox_name.replace('_groupBox', '_ani_widget')

            # Create and add the widget
            pixmap = QPixmap(join(self.image_folder, config['image']))
            scaled_pixmap = pixmap.scaled(300, 450, Qt.AspectRatioMode.KeepAspectRatio)  # Adjust size as needed
            widget = LineAngleWidget(
                scaled_pixmap,
                anchor_x_factor=config['anchor_x'],
                anchor_y_factor=config['anchor_y'],
                line_length_factor=config['line_length']
            )

            setattr(self, widget_name, widget)  # Store widget as class attribute
            layout.addWidget(widget, 1, 0, 1, 2)
            widget.setMinimumSize(300, 400)


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