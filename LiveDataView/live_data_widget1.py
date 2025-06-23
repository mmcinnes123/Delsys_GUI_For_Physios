# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'live_data_widget_1.ui'
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
    QLabel, QSizePolicy, QSpinBox, QTabWidget,
    QWidget)

class Ui_LiveWindow(object):
    def setupUi(self, LiveWindow):
        if not LiveWindow.objectName():
            LiveWindow.setObjectName(u"LiveWindow")
        LiveWindow.resize(1152, 648)
        self.gridLayout = QGridLayout(LiveWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(LiveWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.horizontalLayout = QHBoxLayout(self.tab1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.tab1)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.el_flex_target_label = QLabel(self.groupBox)
        self.el_flex_target_label.setObjectName(u"el_flex_target_label")
        font = QFont()
        font.setPointSize(12)
        self.el_flex_target_label.setFont(font)
        self.el_flex_target_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.el_flex_target_label, 3, 0, 1, 1)

        self.el_flex_value = QLabel(self.groupBox)
        self.el_flex_value.setObjectName(u"el_flex_value")
        font1 = QFont()
        font1.setPointSize(14)
        self.el_flex_value.setFont(font1)
        self.el_flex_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.el_flex_value, 0, 0, 1, 2)

        self.el_flex_target_spinBox = QSpinBox(self.groupBox)
        self.el_flex_target_spinBox.setObjectName(u"el_flex_target_spinBox")
        self.el_flex_target_spinBox.setFont(font)
        self.el_flex_target_spinBox.setMaximum(180)
        self.el_flex_target_spinBox.setSingleStep(10)
        self.el_flex_target_spinBox.setValue(150)

        self.gridLayout_2.addWidget(self.el_flex_target_spinBox, 3, 1, 1, 1)

        self.el_flex_max_label = QLabel(self.groupBox)
        self.el_flex_max_label.setObjectName(u"el_flex_max_label")
        self.el_flex_max_label.setFont(font)
        self.el_flex_max_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.el_flex_max_label, 2, 0, 1, 1)

        self.el_flex_max_value = QLabel(self.groupBox)
        self.el_flex_max_value.setObjectName(u"el_flex_max_value")
        self.el_flex_max_value.setFont(font)

        self.gridLayout_2.addWidget(self.el_flex_max_value, 2, 1, 1, 1)

        self.el_flex_image = QLabel(self.groupBox)
        self.el_flex_image.setObjectName(u"el_flex_image")
        self.el_flex_image.setPixmap(QPixmap(u"./Images/GUI_ElbowFlex.png"))
        self.el_flex_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.el_flex_image, 1, 0, 1, 2)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab1)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab1)
        self.groupBox_3.setObjectName(u"groupBox_3")

        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.tab1)
        self.groupBox_4.setObjectName(u"groupBox_4")

        self.horizontalLayout.addWidget(self.groupBox_4)

        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(LiveWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LiveWindow)
    # setupUi

    def retranslateUi(self, LiveWindow):
        LiveWindow.setWindowTitle(QCoreApplication.translate("LiveWindow", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("LiveWindow", u"Flexion", None))
        self.el_flex_target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.el_flex_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.el_flex_max_label.setText(QCoreApplication.translate("LiveWindow", u"Current Max:", None))
        self.el_flex_max_value.setText(QCoreApplication.translate("LiveWindow", u"Dynamic Max Value", None))
        self.el_flex_image.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("LiveWindow", u"Extension", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("LiveWindow", u"Pronation", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("LiveWindow", u"Supination", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("LiveWindow", u"Elbow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("LiveWindow", u"Shoulder", None))
    # retranslateUi

