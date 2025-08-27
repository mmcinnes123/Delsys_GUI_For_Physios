# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'compass_cal_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_CompassCalibration(object):
    def setupUi(self, CompassCalibration):
        if not CompassCalibration.objectName():
            CompassCalibration.setObjectName(u"CompassCalibration")
        CompassCalibration.resize(772, 657)
        self.gridLayout = QGridLayout(CompassCalibration)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 7, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 7, 1)

        self.label = QLabel(CompassCalibration)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.groupBox = QGroupBox(CompassCalibration)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setPointSize(14)
        self.groupBox.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sensor1_progressBar = QProgressBar(self.groupBox)
        self.sensor1_progressBar.setObjectName(u"sensor1_progressBar")
        self.sensor1_progressBar.setFont(font1)
        self.sensor1_progressBar.setValue(0)

        self.horizontalLayout.addWidget(self.sensor1_progressBar)

        self.sensor1_progressLabel = QLabel(self.groupBox)
        self.sensor1_progressLabel.setObjectName(u"sensor1_progressLabel")
        palette = QPalette()
        brush = QBrush(QColor(0, 199, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.sensor1_progressLabel.setPalette(palette)

        self.horizontalLayout.addWidget(self.sensor1_progressLabel)


        self.gridLayout.addWidget(self.groupBox, 5, 1, 1, 1)

        self.label_2 = QLabel(CompassCalibration)
        self.label_2.setObjectName(u"label_2")
        palette1 = QPalette()
        brush2 = QBrush(QColor(208, 12, 12, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.label_2.setPalette(palette1)
        font2 = QFont()
        font2.setPointSize(12)
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.groupBox_3 = QGroupBox(CompassCalibration)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font1)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sensor3_progressBar = QProgressBar(self.groupBox_3)
        self.sensor3_progressBar.setObjectName(u"sensor3_progressBar")
        self.sensor3_progressBar.setFont(font1)
        self.sensor3_progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.sensor3_progressBar)

        self.sensor3_progressLabel = QLabel(self.groupBox_3)
        self.sensor3_progressLabel.setObjectName(u"sensor3_progressLabel")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.sensor3_progressLabel.setPalette(palette2)

        self.horizontalLayout_3.addWidget(self.sensor3_progressLabel)


        self.gridLayout.addWidget(self.groupBox_3, 7, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(CompassCalibration)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sensor2_progressBar = QProgressBar(self.groupBox_2)
        self.sensor2_progressBar.setObjectName(u"sensor2_progressBar")
        self.sensor2_progressBar.setFont(font1)
        self.sensor2_progressBar.setValue(0)

        self.horizontalLayout_2.addWidget(self.sensor2_progressBar)

        self.sensor2_progressLabel = QLabel(self.groupBox_2)
        self.sensor2_progressLabel.setObjectName(u"sensor2_progressLabel")
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.sensor2_progressLabel.setPalette(palette3)

        self.horizontalLayout_2.addWidget(self.sensor2_progressLabel)


        self.gridLayout.addWidget(self.groupBox_2, 6, 1, 1, 1)

        self.finishButton = QPushButton(CompassCalibration)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setFont(font1)

        self.gridLayout.addWidget(self.finishButton, 9, 1, 1, 1)

        self.resetButton = QPushButton(CompassCalibration)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setFont(font2)

        self.gridLayout.addWidget(self.resetButton, 8, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 10, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.retranslateUi(CompassCalibration)

        QMetaObject.connectSlotsByName(CompassCalibration)
    # setupUi

    def retranslateUi(self, CompassCalibration):
        CompassCalibration.setWindowTitle(QCoreApplication.translate("CompassCalibration", u"Form", None))
        self.label.setText(QCoreApplication.translate("CompassCalibration", u"Calibrate the Compass", None))
        self.groupBox.setTitle(QCoreApplication.translate("CompassCalibration", u"Sensor 1", None))
        self.sensor1_progressLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("CompassCalibration", u"Move each sensor in a figure-of-eight at a steady speed until complete.", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("CompassCalibration", u"Sensor 3", None))
        self.sensor3_progressLabel.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("CompassCalibration", u"Sensor 2", None))
        self.sensor2_progressLabel.setText("")
        self.finishButton.setText(QCoreApplication.translate("CompassCalibration", u"Finish", None))
        self.resetButton.setText(QCoreApplication.translate("CompassCalibration", u"Reset", None))
    # retranslateUi

