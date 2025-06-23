from PySide6.QtCore import Qt
from PySide6.QtWidgets import *


class CollectionMetricsManagement():
    def __init__(self):
        self.collectionmetrics = self.CollectionValuesPanel()
        self.imuTestValues = self.IMUTestValuesPanel()


    def CollectionValuesPanel(self):
        collectionValuesPanel = QWidget()
        collectionvaluesLayout = QVBoxLayout()

        self.pipelinestatelabel = QLabel("-")
        self.pipelinestatelabel.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.pipelinestatelabel.setStyleSheet("color:white")
        collectionvaluesLayout.addWidget(self.pipelinestatelabel)

        self.sensorsconnected = QLabel('-')
        self.sensorsconnected.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.sensorsconnected.setStyleSheet("color : white ")
        collectionvaluesLayout.addWidget(self.sensorsconnected)

        self.totalchannels = QLabel('-')
        self.totalchannels.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.totalchannels.setStyleSheet("color : white ")
        collectionvaluesLayout.addWidget(self.totalchannels)

        self.framescollected = QLabel('-')
        self.framescollected.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.framescollected.setStyleSheet("color : white ")
        collectionvaluesLayout.addWidget(self.framescollected)

        collectionValuesPanel.setFixedWidth(200)
        collectionValuesPanel.setLayout(collectionvaluesLayout)

        return collectionValuesPanel

    def IMUTestValuesPanel(self):
        imuTestValuesPanel = QWidget()
        textvaluesLayout = QVBoxLayout()

        self.senAeul1 = QLabel('-')
        self.senAeul1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.senAeul1.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.senAeul1)

        self.senAeul2 = QLabel('-')
        self.senAeul2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.senAeul2.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.senAeul2)

        self.senAeul3 = QLabel('-')
        self.senAeul3.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.senAeul3.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.senAeul3)

        line1 = QFrame()
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)
        line1.setStyleSheet("background-color: white")
        textvaluesLayout.addWidget(line1)

        self.senBeul1 = QLabel('-')
        self.senBeul1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.senBeul1.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.senBeul1)

        self.senBeul2 = QLabel('-')
        self.senBeul2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.senBeul2.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.senBeul2)

        self.senBeul3 = QLabel('-')
        self.senBeul3.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.senBeul3.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.senBeul3)

        line1 = QFrame()
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)
        line1.setStyleSheet("background-color: white")
        textvaluesLayout.addWidget(line1)

        self.senCeul1 = QLabel('-')
        self.senCeul1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.senCeul1.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.senCeul1)

        self.senCeul2 = QLabel('-')
        self.senCeul2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.senCeul2.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.senCeul2)

        self.senCeul3 = QLabel('-')
        self.senCeul3.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.senCeul3.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.senCeul3)

        imuTestValuesPanel.setFixedWidth(200)
        imuTestValuesPanel.setLayout(textvaluesLayout)

        return imuTestValuesPanel