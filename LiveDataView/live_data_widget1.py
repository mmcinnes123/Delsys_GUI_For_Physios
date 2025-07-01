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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QWidget)

class Ui_LiveWindow(object):
    def setupUi(self, LiveWindow):
        if not LiveWindow.objectName():
            LiveWindow.setObjectName(u"LiveWindow")
        LiveWindow.resize(1152, 648)
        self.gridLayout = QGridLayout(LiveWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(LiveWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.horizontalLayout = QHBoxLayout(self.tab1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.tab1)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setPointSize(16)
        self.groupBox.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.el_flex_target_label = QLabel(self.groupBox)
        self.el_flex_target_label.setObjectName(u"el_flex_target_label")
        self.el_flex_target_label.setFont(font)
        self.el_flex_target_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.el_flex_target_label, 6, 0, 1, 1)

        self.el_flex_image = QLabel(self.groupBox)
        self.el_flex_image.setObjectName(u"el_flex_image")
        self.el_flex_image.setPixmap(QPixmap(u"../Images/GUI_ElbowFlex.png"))
        self.el_flex_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.el_flex_image, 1, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.el_flex_target_spinBox = QSpinBox(self.groupBox)
        self.el_flex_target_spinBox.setObjectName(u"el_flex_target_spinBox")
        self.el_flex_target_spinBox.setFont(font)
        self.el_flex_target_spinBox.setMaximum(180)
        self.el_flex_target_spinBox.setSingleStep(10)
        self.el_flex_target_spinBox.setValue(150)

        self.gridLayout_2.addWidget(self.el_flex_target_spinBox, 6, 1, 1, 1)

        self.el_flex_max_label = QLabel(self.groupBox)
        self.el_flex_max_label.setObjectName(u"el_flex_max_label")
        font2 = QFont()
        font2.setPointSize(18)
        self.el_flex_max_label.setFont(font2)
        self.el_flex_max_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.el_flex_max_label, 3, 0, 1, 1)

        self.el_flex_reset_pushButton = QPushButton(self.groupBox)
        self.el_flex_reset_pushButton.setObjectName(u"el_flex_reset_pushButton")
        self.el_flex_reset_pushButton.setFont(font)

        self.gridLayout_2.addWidget(self.el_flex_reset_pushButton, 4, 0, 1, 2)

        self.el_flex_max_value = QLabel(self.groupBox)
        self.el_flex_max_value.setObjectName(u"el_flex_max_value")
        self.el_flex_max_value.setFont(font2)

        self.gridLayout_2.addWidget(self.el_flex_max_value, 3, 1, 1, 1)

        self.el_flex_value = QLabel(self.groupBox)
        self.el_flex_value.setObjectName(u"el_flex_value")
        font3 = QFont()
        font3.setPointSize(26)
        self.el_flex_value.setFont(font3)
        self.el_flex_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.el_flex_value, 0, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_5 = QGroupBox(self.tab1)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.el_ext_target_label = QLabel(self.groupBox_5)
        self.el_ext_target_label.setObjectName(u"el_ext_target_label")
        self.el_ext_target_label.setFont(font)
        self.el_ext_target_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.el_ext_target_label, 6, 0, 1, 1)

        self.el_flex_image_2 = QLabel(self.groupBox_5)
        self.el_flex_image_2.setObjectName(u"el_flex_image_2")
        self.el_flex_image_2.setPixmap(QPixmap(u"../Images/GUI_ElbowFlex.png"))
        self.el_flex_image_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.el_flex_image_2, 1, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 5, 0, 1, 1)

        self.el_ext_target_spinBox = QSpinBox(self.groupBox_5)
        self.el_ext_target_spinBox.setObjectName(u"el_ext_target_spinBox")
        self.el_ext_target_spinBox.setFont(font)
        self.el_ext_target_spinBox.setMaximum(180)
        self.el_ext_target_spinBox.setSingleStep(10)
        self.el_ext_target_spinBox.setValue(150)

        self.gridLayout_3.addWidget(self.el_ext_target_spinBox, 6, 1, 1, 1)

        self.el_ext_max_label = QLabel(self.groupBox_5)
        self.el_ext_max_label.setObjectName(u"el_ext_max_label")
        self.el_ext_max_label.setFont(font2)
        self.el_ext_max_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.el_ext_max_label, 3, 0, 1, 1)

        self.el_ext_reset_pushButton = QPushButton(self.groupBox_5)
        self.el_ext_reset_pushButton.setObjectName(u"el_ext_reset_pushButton")
        self.el_ext_reset_pushButton.setFont(font)

        self.gridLayout_3.addWidget(self.el_ext_reset_pushButton, 4, 0, 1, 2)

        self.el_ext_max_value = QLabel(self.groupBox_5)
        self.el_ext_max_value.setObjectName(u"el_ext_max_value")
        self.el_ext_max_value.setFont(font2)

        self.gridLayout_3.addWidget(self.el_ext_max_value, 3, 1, 1, 1)

        self.el_ext_value = QLabel(self.groupBox_5)
        self.el_ext_value.setObjectName(u"el_ext_value")
        self.el_ext_value.setFont(font3)
        self.el_ext_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.el_ext_value, 0, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.tab1)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font1)
        self.gridLayout_5 = QGridLayout(self.groupBox_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.el_pro_target_label = QLabel(self.groupBox_6)
        self.el_pro_target_label.setObjectName(u"el_pro_target_label")
        self.el_pro_target_label.setFont(font)
        self.el_pro_target_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.el_pro_target_label, 6, 0, 1, 1)

        self.el_flex_image_4 = QLabel(self.groupBox_6)
        self.el_flex_image_4.setObjectName(u"el_flex_image_4")
        self.el_flex_image_4.setPixmap(QPixmap(u"../Images/GUI_ElbowFlex.png"))
        self.el_flex_image_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.el_flex_image_4, 1, 0, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 5, 0, 1, 1)

        self.el_pro_target_spinBox = QSpinBox(self.groupBox_6)
        self.el_pro_target_spinBox.setObjectName(u"el_pro_target_spinBox")
        self.el_pro_target_spinBox.setFont(font)
        self.el_pro_target_spinBox.setMaximum(180)
        self.el_pro_target_spinBox.setSingleStep(10)
        self.el_pro_target_spinBox.setValue(150)

        self.gridLayout_5.addWidget(self.el_pro_target_spinBox, 6, 1, 1, 1)

        self.el_pro_max_label = QLabel(self.groupBox_6)
        self.el_pro_max_label.setObjectName(u"el_pro_max_label")
        self.el_pro_max_label.setFont(font2)
        self.el_pro_max_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.el_pro_max_label, 3, 0, 1, 1)

        self.el_pro_reset_pushButton = QPushButton(self.groupBox_6)
        self.el_pro_reset_pushButton.setObjectName(u"el_pro_reset_pushButton")
        self.el_pro_reset_pushButton.setFont(font)

        self.gridLayout_5.addWidget(self.el_pro_reset_pushButton, 4, 0, 1, 2)

        self.el_pro_max_value = QLabel(self.groupBox_6)
        self.el_pro_max_value.setObjectName(u"el_pro_max_value")
        self.el_pro_max_value.setFont(font2)

        self.gridLayout_5.addWidget(self.el_pro_max_value, 3, 1, 1, 1)

        self.el_pro_value = QLabel(self.groupBox_6)
        self.el_pro_value.setObjectName(u"el_pro_value")
        self.el_pro_value.setFont(font3)
        self.el_pro_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.el_pro_value, 0, 0, 1, 2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.tab1)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font1)
        self.gridLayout_6 = QGridLayout(self.groupBox_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.el_sup_target_label = QLabel(self.groupBox_7)
        self.el_sup_target_label.setObjectName(u"el_sup_target_label")
        self.el_sup_target_label.setFont(font)
        self.el_sup_target_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.el_sup_target_label, 6, 0, 1, 1)

        self.el_flex_image_5 = QLabel(self.groupBox_7)
        self.el_flex_image_5.setObjectName(u"el_flex_image_5")
        self.el_flex_image_5.setPixmap(QPixmap(u"../Images/GUI_ElbowFlex.png"))
        self.el_flex_image_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.el_flex_image_5, 1, 0, 1, 2)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_9, 5, 0, 1, 1)

        self.el_sup_target_spinBox = QSpinBox(self.groupBox_7)
        self.el_sup_target_spinBox.setObjectName(u"el_sup_target_spinBox")
        self.el_sup_target_spinBox.setFont(font)
        self.el_sup_target_spinBox.setMaximum(180)
        self.el_sup_target_spinBox.setSingleStep(10)
        self.el_sup_target_spinBox.setValue(150)

        self.gridLayout_6.addWidget(self.el_sup_target_spinBox, 6, 1, 1, 1)

        self.el_sup_max_label = QLabel(self.groupBox_7)
        self.el_sup_max_label.setObjectName(u"el_sup_max_label")
        self.el_sup_max_label.setFont(font2)
        self.el_sup_max_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.el_sup_max_label, 3, 0, 1, 1)

        self.el_sup_reset_pushButton = QPushButton(self.groupBox_7)
        self.el_sup_reset_pushButton.setObjectName(u"el_sup_reset_pushButton")
        self.el_sup_reset_pushButton.setFont(font)

        self.gridLayout_6.addWidget(self.el_sup_reset_pushButton, 4, 0, 1, 2)

        self.el_sup_max_value = QLabel(self.groupBox_7)
        self.el_sup_max_value.setObjectName(u"el_sup_max_value")
        self.el_sup_max_value.setFont(font2)

        self.gridLayout_6.addWidget(self.el_sup_max_value, 3, 1, 1, 1)

        self.el_sup_value = QLabel(self.groupBox_7)
        self.el_sup_value.setObjectName(u"el_sup_value")
        self.el_sup_value.setFont(font3)
        self.el_sup_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.el_sup_value, 0, 0, 1, 2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_10, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_7)

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
        self.el_flex_image.setText("")
        self.el_flex_max_label.setText(QCoreApplication.translate("LiveWindow", u"Max:", None))
        self.el_flex_reset_pushButton.setText(QCoreApplication.translate("LiveWindow", u"Reset", None))
        self.el_flex_max_value.setText(QCoreApplication.translate("LiveWindow", u"MaxVal", None))
        self.el_flex_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("LiveWindow", u"Extension", None))
        self.el_ext_target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.el_flex_image_2.setText("")
        self.el_ext_max_label.setText(QCoreApplication.translate("LiveWindow", u"Min:", None))
        self.el_ext_reset_pushButton.setText(QCoreApplication.translate("LiveWindow", u"Reset", None))
        self.el_ext_max_value.setText(QCoreApplication.translate("LiveWindow", u"MaxVal", None))
        self.el_ext_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("LiveWindow", u"Pronation", None))
        self.el_pro_target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.el_flex_image_4.setText("")
        self.el_pro_max_label.setText(QCoreApplication.translate("LiveWindow", u"Min:", None))
        self.el_pro_reset_pushButton.setText(QCoreApplication.translate("LiveWindow", u"Reset", None))
        self.el_pro_max_value.setText(QCoreApplication.translate("LiveWindow", u"MaxVal", None))
        self.el_pro_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("LiveWindow", u"Supination", None))
        self.el_sup_target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.el_flex_image_5.setText("")
        self.el_sup_max_label.setText(QCoreApplication.translate("LiveWindow", u"Min:", None))
        self.el_sup_reset_pushButton.setText(QCoreApplication.translate("LiveWindow", u"Reset", None))
        self.el_sup_max_value.setText(QCoreApplication.translate("LiveWindow", u"MaxVal", None))
        self.el_sup_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("LiveWindow", u"Elbow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("LiveWindow", u"Shoulder", None))
    # retranslateUi

