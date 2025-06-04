from PySide6.QtCore import Qt
from PySide6.QtWidgets import *


class IMUMetricsManagement():
    def __init__(self):
        self.imuValues = self.IMUValuesPanel()


    def IMUValuesPanel(self):
        collectionValuesPanel = QWidget()
        collectionvaluesLayout = QVBoxLayout()

        self.myMetric = QLabel('-')
        self.myMetric.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.myMetric.setStyleSheet("color : white ")
        collectionvaluesLayout.addWidget(self.myMetric)

        collectionValuesPanel.setFixedWidth(200)
        collectionValuesPanel.setLayout(collectionvaluesLayout)

        return collectionValuesPanel