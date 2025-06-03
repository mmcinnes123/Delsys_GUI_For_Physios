import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class LiveDataWindow(QWidget):

    def __init__(self, controller):
        QWidget.__init__(self)
        self.controller = controller
        grid = QGridLayout()
        self.setStyleSheet("background-color:#3d4c51;")
        self.setWindowTitle("Start Menu")

        imageBox = QVBoxLayout()
        self.im = QPixmap("./Images/delsys.png")
        self.label = QLabel()
        self.label.setPixmap(self.im)
        self.label.setAlignment(Qt.AlignCenter)
        imageBox.addWidget(self.label)
        imageBox.setAlignment(Qt.AlignBaseline)
        imageBox.setContentsMargins(0,100,0,0)
        grid.addLayout(imageBox, 0, 0)

        errorbox = QHBoxLayout()
        errorbox.setSpacing(0)
        self.error = QLabel()
        self.error.setText("")
        self.error.setAlignment(Qt.AlignHCenter)
        self.error.setStyleSheet('QLabel {color: red;}')
        errorbox.addWidget(self.error)
        errorbox.setAlignment(Qt.AlignRight)
        grid.addLayout(errorbox,1,0)

        buttonBox = QHBoxLayout()
        buttonBox.setSpacing(0)

        button = QPushButton('Connect', self)
        button.setToolTip('Collect Data')
        button.objectName = 'Collect'
        button.clicked.connect(self.Do_Nothing_Callback)
        button.setFixedSize(200, 100)
        button.setStyleSheet('QPushButton {color: white;}')
        buttonBox.addWidget(button)

        grid.addLayout(buttonBox, 2, 0)

        self.setLayout(grid)
        self.setFixedSize(self.width(), self.height())

    def Do_Nothing_Callback(self):

        print('This button does nothing')

