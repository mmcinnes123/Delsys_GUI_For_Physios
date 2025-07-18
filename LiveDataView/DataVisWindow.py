
import sys
from os.path import join

from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap, QColor
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

        # Define joint mapping: (attribute_name, value_widget, max_value_widget)
        self.joint_mapping = {
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


        if self.controller:  # Don't run if just testing UI

            self.connector = self.controller.collectWindow.CallbackConnector

            # Reset all max values
            for joint_name in self.joint_mapping:
                if joint_name in ['el_flex', 'el_ext']:
                    setattr(self.connector, f"{joint_name}_max", 90)
                else:
                    setattr(self.connector, f"{joint_name}_max", 0)

            # Set button functionalities
            for joint_name in self.joint_mapping:
                button = getattr(self, f"{joint_name}_reset_pushButton")
                button.clicked.connect(lambda checked, j=joint_name: self.reset_buttonCallback(j))

            # Create a timer to update the display
            self.update_timer = QTimer()
            self.update_timer.timeout.connect(self.update_display)
            self.update_timer.start(100)  # Update every 100ms

    # -----------------------------------------------------------------------
    # ---- Callback Functions

    def update_display(self):

        for joint_name, (value_widget, max_widget, groupbox, ani_widget) in self.joint_mapping.items():
            if hasattr(self.connector, joint_name):
                joint_value = getattr(self.connector, joint_name)
                max_value = getattr(self.connector, f"{joint_name}_max")
                target_value = getattr(self, f"{joint_name}_target_spinBox").value()

                if joint_value is not None:
                    value_widget.setText(f"{joint_value:.0f}°")
                    self.toggle_groupbox_state(groupbox, ani_widget, True)  # Enable groupbox
                    ani_widget.set_angle(joint_value)  # Update the animation angle
                    ani_widget.set_maxangle(max_value)
                    ani_widget.set_target(target_value)
                else:
                    value_widget.setText("-°")
                    self.toggle_groupbox_state(groupbox, ani_widget, False)  # Disable groupbox
                    # ani_widget.set_angle(0)  # Reset animation to 0 when no value
                    ani_widget.set_target(target_value)


                if max_value is not None:
                    max_widget.setText(f"{max_value:.0f}°")
                else:
                    max_widget.setText("-°")

    def closeEvent(self, event):
        if self.controller:
            self.connector.vis_dataFlag = False
            self.controller.collectWindow.start_vis_button.setEnabled(True)
            self.controller.collectWindow.start_vis_button.setStyleSheet("color : white")
        event.accept()  # Allow the window to close

    # --- Reset Button callback

    def reset_buttonCallback(self, joint_name):

        """ When reset buttons are clicked, Max value is set to current value of that joint angle, or 0 if joint angle is None"""

        if hasattr(self.connector, joint_name):
            current_value = getattr(self.connector, joint_name)

            if current_value is not None:
                setattr(self.connector, f"{joint_name}_max", current_value)
            else:
                if joint_name in ['el_flex', 'el_ext']:
                    setattr(self.connector, f"{joint_name}_max", 90)
                else:
                    setattr(self.connector, f"{joint_name}_max", 0)

    # --- Other functions

    def setup_joint_animations(self):
        """
        Sets up animation widgets for all joint angles by adding LineAngleWidgets
        to their respective groupBoxes.
        """
        # Dictionary mapping configurations for the live visualisation to the groupBox for each joint angle
        joint_mappings = {
            'sh_flex_groupBox': {
                'image': "sh_flex_image.png", # The name of the image file in the Images folder
                'anchor_x': 0.28,    # The x-coordinate where the red line begins (as fraction of the widget width, from left)
                'anchor_y': 0.4,    # The y-coordinate where the red line begins (as fraction of the widget height, from top down)
                'line_length': 0.45, # The length of the red line
                'rotation_dir': -1, # Whether the line should sweep in the opposite direction (1 or -1)
                'extra_rotation': 0 # Whether the line should begin from a different orientation (-90, 90, 180, etc)
            },
            'sh_abd_groupBox': {
                'image': "sh_abd_image.png",
                'anchor_x': 0.6,
                'anchor_y': 0.43,
                'line_length': 0.45,
                'rotation_dir': 1,
                'extra_rotation': 0
            },
            'sh_introt_groupBox': {
                'image': "sh_introt_image.png",
                'anchor_x': 0.58,
                'anchor_y': 0.61,
                'line_length': 0.45,
                'rotation_dir': -1,
                'extra_rotation': 180
            },
            'sh_extrot_groupBox': {
                'image': "sh_extrot_image.png",
                'anchor_x': 0.58,
                'anchor_y': 0.61,
                'line_length': 0.45,
                'rotation_dir': 1,
                'extra_rotation': 180
            },
            'el_flex_groupBox': {
                'image': "el_flex_image.png",
                'anchor_x': 0.34,
                'anchor_y': 0.60,
                'line_length': 0.35,
                'rotation_dir': -1,
                'extra_rotation': 0
            },
            'el_ext_groupBox': {
                'image': "el_ext_image.png",
                'anchor_x': 0.34,
                'anchor_y': 0.60,
                'line_length': 0.35,
                'rotation_dir': -1,
                'extra_rotation': 0
            },
            'el_pro_groupBox': {
                'image': "el_pro_image.png",
                'anchor_x': 0.38,
                'anchor_y': 0.60,
                'line_length': 0.3,
                'rotation_dir': 1,
                'extra_rotation': 180
            },
            'el_sup_groupBox': {
                'image': "el_sup_image.png",
                'anchor_x': 0.38,
                'anchor_y': 0.60,
                'line_length': 0.3,
                'rotation_dir': -1,
                'extra_rotation': 180
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
            # scaled_pixmap = pixmap.scaled(300, 450, Qt.AspectRatioMode.KeepAspectRatio)  # Adjust size as needed
            widget = LineAngleWidget(
                pixmap,
                anchor_x_factor=config['anchor_x'],
                anchor_y_factor=config['anchor_y'],
                line_length_factor=config['line_length'],
                rotation_dir=config['rotation_dir'],
                extra_rotation=config['extra_rotation']
            )

            setattr(self, widget_name, widget)  # Store widget as class attribute
            layout.addWidget(widget, 1, 0, 1, 2)
            widget.setMinimumSize(300, 400)


    def toggle_groupbox_state(self, groupbox, ani_widget, enabled=True):

        if enabled:
            # Reset to default style (black text)
            groupbox.setStyleSheet("")
            ani_widget._pen.setColor(QColor(0, 0, 255, 128))
            ani_widget._maxline_pen.setColor(Qt.blue)
            ani_widget._target_pen.setColor(Qt.red)

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

            # Grey the red line
            ani_widget._pen.setColor(Qt.gray)
            ani_widget._maxline_pen.setColor(Qt.gray)
            ani_widget._target_pen.setColor(Qt.gray)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = DataVisWindow(None)
    window.show()

    sys.exit(app.exec())