import numpy as np
import qmt
np.set_printoptions(suppress=True)

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtCore    import Qt, QTimer, Slot
from PySide6.QtGui     import QPainter, QPen
import math
import sys
import random    # stand‑in for your live sensor


class LineAngleWidget(QWidget):
    """
    A widget that draws a single red line whose angle (in degrees)
    is controlled via set_angle(). The left end of the line is fixed.
    """
    def __init__(self, pixmap, parent=None, anchor_x_factor=0.5, anchor_y_factor=0.5, line_length_factor=0.2, rotation_dir=1, extra_rotation=0):
        super().__init__(parent)
        self._pix = pixmap
        if self._pix.isNull():
            print("Warning: Pixmap failed to load!")
        self._angle = 0.0                      # in degrees
        self._pen   = QPen(Qt.red, 4, Qt.SolidLine, Qt.RoundCap)
        self.setAttribute(Qt.WA_TranslucentBackground)  # lets the image show through
        self._anchor_x_factor = anchor_x_factor  # percentage of width
        self._anchor_y_factor = anchor_y_factor  # percentage of height
        self._line_length_factor = line_length_factor
        self._rotation_dir = rotation_dir
        self._extra_rotation = extra_rotation

    @Slot(float)
    def set_angle(self, angle_deg: float):
        """Update the line’s angle and repaint."""
        self._angle = angle_deg % 360
        self.update()

    def paintEvent(self, event):

        w, h = self.width(), self.height()
        anchor_x = int(w * self._anchor_x_factor)  # Use factor instead of fixed position
        anchor_y = int(h * self._anchor_y_factor)
        line_length = w * self._line_length_factor


        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Scale pixmap to fit widget size while maintaining aspect ratio
        scaled_pixmap = self._pix.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Calculate position to center the pixmap
        x = (w - scaled_pixmap.width()) // 2
        y = (h - scaled_pixmap.height()) // 2

        # --- 1. draw the background image ---
        painter.drawPixmap(x, y, scaled_pixmap)

        painter.translate(anchor_x, anchor_y)
        painter.rotate(self._rotation_dir * self._angle + self._extra_rotation)           # rotate CCW by default
        painter.setPen(self._pen)

        # Draw line from fixed anchor (0,0) to right
        painter.drawLine(0, 0, 0, line_length)

        painter.end()

# --------------------------------------------------------------
def main():
    app = QApplication(sys.argv)

    widget = LineAngleWidget()
    widget.setMinimumSize(300, 300)

    # Simulate live data updates with a timer
    def fake_sensor_reading():
        widget.set_angle(random.uniform(-20, 20))  # swing ±90°

    timer = QTimer(interval=200, timeout=fake_sensor_reading)
    timer.start()

    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
