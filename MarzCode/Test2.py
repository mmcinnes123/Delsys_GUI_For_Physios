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
    def __init__(self, parent=None):
        super().__init__(parent)
        self._angle = 0.0                      # in degrees
        self._pen   = QPen(Qt.red, 4, Qt.SolidLine, Qt.RoundCap)

    @Slot(float)
    def set_angle(self, angle_deg: float):
        """Update the line’s angle and repaint."""
        self._angle = angle_deg % 360
        self.update()

    def paintEvent(self, event):
        w, h = self.width(), self.height()
        anchor_x = w // 2                          # margin from left
        anchor_y = h // 2                      # vertically centered

        line_length = 0.5 * w                  # 80% of width

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(anchor_x, anchor_y)
        painter.rotate(-self._angle)           # rotate CCW by default
        painter.setPen(self._pen)

        # Draw line from fixed anchor (0,0) to right
        painter.drawLine(0, 0, line_length, 0)

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
