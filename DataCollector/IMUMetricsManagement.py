from PySide6.QtCore import Qt
from PySide6.QtWidgets import *


class IMUMetricsManagement():
    def __init__(self):
        self.imuTestValues = self.IMUTestValuesPanel()


    def IMUTestValuesPanel(self):
        collectionValuesPanel = QWidget()
        collectionvaluesLayout = QVBoxLayout()

        self.senAeul1 = QLabel('-')
        self.senAeul1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.senAeul1.setStyleSheet("color : white ")
        collectionvaluesLayout.addWidget(self.senAeul1)

        self.senAeul2 = QLabel('-')
        self.senAeul2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.senAeul2.setStyleSheet("color : white ")
        collectionvaluesLayout.addWidget(self.senAeul2)

        self.senAeul3 = QLabel('-')
        self.senAeul3.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.senAeul3.setStyleSheet("color : white ")
        collectionvaluesLayout.addWidget(self.senAeul3)

        collectionValuesPanel.setFixedWidth(200)
        collectionValuesPanel.setLayout(collectionvaluesLayout)

        return collectionValuesPanel