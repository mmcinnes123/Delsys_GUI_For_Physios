# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibration_widget3.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_calibrationWindow(object):
    def setupUi(self, calibrationWindow):
        if not calibrationWindow.objectName():
            calibrationWindow.setObjectName(u"calibrationWindow")
        calibrationWindow.resize(1145, 657)
        self.gridLayout_3 = QGridLayout(calibrationWindow)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 0, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 3, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(112, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 3, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 6, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(670, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 3, 3, 1, 2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_12, 3, 5, 1, 1)

        self.groupBox = QGroupBox(calibrationWindow)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
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
        font1 = QFont()
        font1.setPointSize(14)
        self.calposeButton.setFont(font1)

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
        font2 = QFont()
        font2.setPointSize(12)
        font2.setItalic(False)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.pose_statusMessage = QLabel(self.groupBox)
        self.pose_statusMessage.setObjectName(u"pose_statusMessage")
        palette1 = QPalette()
        brush2 = QBrush(QColor(0, 199, 0, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.pose_statusMessage.setPalette(palette1)
        self.pose_statusMessage.setFont(font)
        self.pose_statusMessage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.pose_statusMessage, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 2, 3, 1, 2)

        self.finishButton = QPushButton(calibrationWindow)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setFont(font1)

        self.gridLayout_3.addWidget(self.finishButton, 7, 3, 1, 2)

        self.horizontalSpacer_11 = QSpacerItem(110, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_11, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(calibrationWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 5, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 1, 5, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 1, 1, 1, 1)

        self.wrist_progressBar = QProgressBar(self.groupBox_2)
        self.wrist_progressBar.setObjectName(u"wrist_progressBar")
        self.wrist_progressBar.setFont(font1)
        self.wrist_progressBar.setValue(0)

        self.gridLayout_2.addWidget(self.wrist_progressBar, 3, 3, 1, 1)

        self.calmove_startButton = QPushButton(self.groupBox_2)
        self.calmove_startButton.setObjectName(u"calmove_startButton")
        self.calmove_startButton.setFont(font1)

        self.gridLayout_2.addWidget(self.calmove_startButton, 1, 2, 1, 2)

        self.horizontalSpacer_7 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.move_statusMessage = QLabel(self.groupBox_2)
        self.move_statusMessage.setObjectName(u"move_statusMessage")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.move_statusMessage.setPalette(palette2)
        self.move_statusMessage.setFont(font)
        self.move_statusMessage.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.move_statusMessage, 4, 2, 1, 2)

        self.elbow_progressBar = QProgressBar(self.groupBox_2)
        self.elbow_progressBar.setObjectName(u"elbow_progressBar")
        self.elbow_progressBar.setFont(font1)
        self.elbow_progressBar.setValue(0)

        self.gridLayout_2.addWidget(self.elbow_progressBar, 3, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 2, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 1, 4, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.label_5.setPalette(palette3)
        font3 = QFont()
        font3.setPointSize(12)
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 4)


        self.gridLayout_3.addWidget(self.groupBox_2, 4, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 8, 3, 1, 2)

        self.step1_groupBox = QGroupBox(calibrationWindow)
        self.step1_groupBox.setObjectName(u"step1_groupBox")
        self.step1_groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.step1_groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.gridLayout_3.addWidget(self.step1_groupBox, 2, 1, 3, 1)

        self.horizontalSpacer_6 = QSpacerItem(112, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 3, 6, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_13, 3, 0, 1, 1)


        self.retranslateUi(calibrationWindow)

        QMetaObject.connectSlotsByName(calibrationWindow)
    # setupUi

    def retranslateUi(self, calibrationWindow):
        calibrationWindow.setWindowTitle(QCoreApplication.translate("calibrationWindow", u"Subject Set Up", None))
        self.groupBox.setTitle(QCoreApplication.translate("calibrationWindow", u"Step 2. Stand or Sit Upright", None))
        self.calposeButton.setText(QCoreApplication.translate("calibrationWindow", u"Click When Holding Pose", None))
        self.label_4.setText(QCoreApplication.translate("calibrationWindow", u"It's important the subject's chest is upright and straight.", None))
        self.pose_statusMessage.setText("")
        self.finishButton.setText(QCoreApplication.translate("calibrationWindow", u"Finish", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("calibrationWindow", u"Step 2. Bend the Elbow and Twist the Wrist", None))
        self.label_3.setText(QCoreApplication.translate("calibrationWindow", u"Wrist", None))
        self.calmove_startButton.setText(QCoreApplication.translate("calibrationWindow", u"Click To Start", None))
        self.move_statusMessage.setText("")
        self.label_2.setText(QCoreApplication.translate("calibrationWindow", u"Elbow", None))
        self.label_5.setText(QCoreApplication.translate("calibrationWindow", u"Ask or help the patient to bend the elbow and twist their wrist back and fourth.", None))
        self.step1_groupBox.setTitle(QCoreApplication.translate("calibrationWindow", u"Step 1. Attach the Sensors", None))
    # retranslateUi

