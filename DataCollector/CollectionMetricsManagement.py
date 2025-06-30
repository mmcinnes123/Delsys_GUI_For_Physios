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

        self.sen1eul1 = QLabel('-')
        self.sen1eul1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.sen1eul1.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.sen1eul1)

        self.sen1eul2 = QLabel('-')
        self.sen1eul2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.sen1eul2.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.sen1eul2)

        self.sen1eul3 = QLabel('-')
        self.sen1eul3.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.sen1eul3.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.sen1eul3)

        line1 = QFrame()
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)
        line1.setStyleSheet("background-color: white")
        textvaluesLayout.addWidget(line1)

        self.sen2eul1 = QLabel('-')
        self.sen2eul1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.sen2eul1.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.sen2eul1)

        self.sen2eul2 = QLabel('-')
        self.sen2eul2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.sen2eul2.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.sen2eul2)

        self.sen2eul3 = QLabel('-')
        self.sen2eul3.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.sen2eul3.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.sen2eul3)

        line1 = QFrame()
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)
        line1.setStyleSheet("background-color: white")
        textvaluesLayout.addWidget(line1)

        self.sen3eul1 = QLabel('-')
        self.sen3eul1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.sen3eul1.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.sen3eul1)

        self.sen3eul2 = QLabel('-')
        self.sen3eul2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.sen3eul2.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.sen3eul2)

        self.sen3eul3 = QLabel('-')
        self.sen3eul3.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.sen3eul3.setStyleSheet("color : white ")
        textvaluesLayout.addWidget(self.sen3eul3)

        imuTestValuesPanel.setFixedWidth(200)
        imuTestValuesPanel.setLayout(textvaluesLayout)

        return imuTestValuesPanel