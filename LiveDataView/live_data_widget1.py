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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpinBox, QWidget)

class Ui_LiveWindow(object):
    def setupUi(self, LiveWindow):
        if not LiveWindow.objectName():
            LiveWindow.setObjectName(u"LiveWindow")
        LiveWindow.resize(378, 293)
        self.gridLayout = QGridLayout(LiveWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(LiveWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.target_spinBox = QSpinBox(self.groupBox)
        self.target_spinBox.setObjectName(u"target_spinBox")
        self.target_spinBox.setAlignment(Qt.AlignCenter)
        self.target_spinBox.setMaximum(180)
        self.target_spinBox.setSingleStep(10)
        self.target_spinBox.setValue(150)

        self.gridLayout_2.addWidget(self.target_spinBox, 2, 1, 1, 1)

        self.target_label = QLabel(self.groupBox)
        self.target_label.setObjectName(u"target_label")
        self.target_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.target_label, 2, 0, 1, 1)

        self.latest_max_value = QLabel(self.groupBox)
        self.latest_max_value.setObjectName(u"latest_max_value")
        self.latest_max_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.latest_max_value, 1, 1, 1, 1)

        self.latest_max_label = QLabel(self.groupBox)
        self.latest_max_label.setObjectName(u"latest_max_label")
        self.latest_max_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.latest_max_label, 1, 0, 1, 1)

        self.current_angle = QLabel(self.groupBox)
        self.current_angle.setObjectName(u"current_angle")
        self.current_angle.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.current_angle, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(LiveWindow)

        QMetaObject.connectSlotsByName(LiveWindow)
    # setupUi

    def retranslateUi(self, LiveWindow):
        LiveWindow.setWindowTitle(QCoreApplication.translate("LiveWindow", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("LiveWindow", u"Elbow", None))
        self.target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.latest_max_value.setText(QCoreApplication.translate("LiveWindow", u"Dynamic Max Value", None))
        self.latest_max_label.setText(QCoreApplication.translate("LiveWindow", u"Latest Max:", None))
        self.current_angle.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
    # retranslateUi

