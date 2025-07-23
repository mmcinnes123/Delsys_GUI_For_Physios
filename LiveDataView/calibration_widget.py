# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibration_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_calibrationWindow(object):
    def setupUi(self, calibrationWindow):
        if not calibrationWindow.objectName():
            calibrationWindow.setObjectName(u"calibrationWindow")
        calibrationWindow.resize(1025, 681)
        self.gridLayout_3 = QGridLayout(calibrationWindow)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 1, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 6, 1, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 4, 0, 1, 1)

        self.label = QLabel(calibrationWindow)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(670, 138, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 4, 1, 1, 2)

        self.groupBox = QGroupBox(calibrationWindow)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setPointSize(20)
        self.groupBox.setFont(font1)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.calposeButton = QPushButton(self.groupBox)
        self.calposeButton.setObjectName(u"calposeButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calposeButton.sizePolicy().hasHeightForWidth())
        self.calposeButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(14)
        self.calposeButton.setFont(font2)

        self.gridLayout.addWidget(self.calposeButton, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        palette = QPalette()
        brush = QBrush(QColor(216, 21, 21, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.label_4.setPalette(palette)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setItalic(False)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.pose_statusMessage = QLabel(self.groupBox)
        self.pose_statusMessage.setObjectName(u"pose_statusMessage")
        palette1 = QPalette()
        brush2 = QBrush(QColor(0, 220, 0, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.pose_statusMessage.setPalette(palette1)
        font4 = QFont()
        font4.setPointSize(16)
        self.pose_statusMessage.setFont(font4)
        self.pose_statusMessage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.pose_statusMessage, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 3, 1, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(calibrationWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.label_5.setPalette(palette2)
        font5 = QFont()
        font5.setPointSize(12)
        self.label_5.setFont(font5)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 2)

        self.calmove_startButton = QPushButton(self.groupBox_2)
        self.calmove_startButton.setObjectName(u"calmove_startButton")
        self.calmove_startButton.setFont(font2)

        self.gridLayout_2.addWidget(self.calmove_startButton, 1, 1, 1, 1)

        self.calmove_endButton = QPushButton(self.groupBox_2)
        self.calmove_endButton.setObjectName(u"calmove_endButton")
        self.calmove_endButton.setFont(font2)

        self.gridLayout_2.addWidget(self.calmove_endButton, 1, 2, 1, 1)

        self.move_statusMessage = QLabel(self.groupBox_2)
        self.move_statusMessage.setObjectName(u"move_statusMessage")
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.move_statusMessage.setPalette(palette3)
        self.move_statusMessage.setFont(font4)
        self.move_statusMessage.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.move_statusMessage, 2, 1, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_2, 5, 1, 1, 2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 4, 3, 1, 1)


        self.retranslateUi(calibrationWindow)

        QMetaObject.connectSlotsByName(calibrationWindow)
    # setupUi

    def retranslateUi(self, calibrationWindow):
        calibrationWindow.setWindowTitle(QCoreApplication.translate("calibrationWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("calibrationWindow", u"Calibrate the Joint Angles", None))
        self.groupBox.setTitle(QCoreApplication.translate("calibrationWindow", u"Step 1. Stand or Sit Upright", None))
        self.calposeButton.setText(QCoreApplication.translate("calibrationWindow", u"Click When Holding Pose", None))
        self.label_4.setText(QCoreApplication.translate("calibrationWindow", u"It's important the subject's chest is upright and straight.", None))
        self.pose_statusMessage.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("calibrationWindow", u"Step 2. Bend the Elbow and Twist the Wrist", None))
        self.label_5.setText(QCoreApplication.translate("calibrationWindow", u"Ask or help the subject to bend the elbow and twist their wrist back and fourth approx. 5 times", None))
        self.calmove_startButton.setText(QCoreApplication.translate("calibrationWindow", u"Click When Starting", None))
        self.calmove_endButton.setText(QCoreApplication.translate("calibrationWindow", u"Click When Done", None))
        self.move_statusMessage.setText("")
    # retranslateUi

