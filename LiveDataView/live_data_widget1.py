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
        LiveWindow.resize(1154, 655)
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
        self.el_flex_groupBox = QGroupBox(self.tab1)
        self.el_flex_groupBox.setObjectName(u"el_flex_groupBox")
        font1 = QFont()
        font1.setPointSize(16)
        self.el_flex_groupBox.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.el_flex_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.el_flex_value = QLabel(self.el_flex_groupBox)
        self.el_flex_value.setObjectName(u"el_flex_value")
        font2 = QFont()
        font2.setPointSize(26)
        self.el_flex_value.setFont(font2)
        self.el_flex_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.el_flex_value, 0, 0, 1, 2)

        self.el_flex_target_spinBox = QSpinBox(self.el_flex_groupBox)
        self.el_flex_target_spinBox.setObjectName(u"el_flex_target_spinBox")
        self.el_flex_target_spinBox.setFont(font)
        self.el_flex_target_spinBox.setMaximum(180)
        self.el_flex_target_spinBox.setSingleStep(10)
        self.el_flex_target_spinBox.setValue(150)

        self.gridLayout_2.addWidget(self.el_flex_target_spinBox, 5, 1, 1, 1)

        self.el_flex_reset_pushButton = QPushButton(self.el_flex_groupBox)
        self.el_flex_reset_pushButton.setObjectName(u"el_flex_reset_pushButton")
        self.el_flex_reset_pushButton.setFont(font)

        self.gridLayout_2.addWidget(self.el_flex_reset_pushButton, 3, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.el_flex_max_value = QLabel(self.el_flex_groupBox)
        self.el_flex_max_value.setObjectName(u"el_flex_max_value")
        palette = QPalette()
        brush = QBrush(QColor(216, 8, 8, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.el_flex_max_value.setPalette(palette)
        font3 = QFont()
        font3.setPointSize(18)
        self.el_flex_max_value.setFont(font3)

        self.gridLayout_2.addWidget(self.el_flex_max_value, 2, 1, 1, 1)

        self.el_flex_target_label = QLabel(self.el_flex_groupBox)
        self.el_flex_target_label.setObjectName(u"el_flex_target_label")
        self.el_flex_target_label.setFont(font)
        self.el_flex_target_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.el_flex_target_label, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.el_flex_max_label = QLabel(self.el_flex_groupBox)
        self.el_flex_max_label.setObjectName(u"el_flex_max_label")
        self.el_flex_max_label.setFont(font3)
        self.el_flex_max_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.el_flex_max_label, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.el_flex_groupBox)

        self.el_ext_groupBox = QGroupBox(self.tab1)
        self.el_ext_groupBox.setObjectName(u"el_ext_groupBox")
        self.el_ext_groupBox.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.el_ext_groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.el_ext_target_label = QLabel(self.el_ext_groupBox)
        self.el_ext_target_label.setObjectName(u"el_ext_target_label")
        self.el_ext_target_label.setFont(font)
        self.el_ext_target_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.el_ext_target_label, 5, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.el_ext_target_spinBox = QSpinBox(self.el_ext_groupBox)
        self.el_ext_target_spinBox.setObjectName(u"el_ext_target_spinBox")
        self.el_ext_target_spinBox.setFont(font)
        self.el_ext_target_spinBox.setMaximum(180)
        self.el_ext_target_spinBox.setSingleStep(10)
        self.el_ext_target_spinBox.setValue(150)

        self.gridLayout_3.addWidget(self.el_ext_target_spinBox, 5, 1, 1, 1)

        self.el_ext_max_label = QLabel(self.el_ext_groupBox)
        self.el_ext_max_label.setObjectName(u"el_ext_max_label")
        self.el_ext_max_label.setFont(font3)
        self.el_ext_max_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.el_ext_max_label, 2, 0, 1, 1)

        self.el_ext_max_value = QLabel(self.el_ext_groupBox)
        self.el_ext_max_value.setObjectName(u"el_ext_max_value")
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.el_ext_max_value.setPalette(palette1)
        self.el_ext_max_value.setFont(font3)

        self.gridLayout_3.addWidget(self.el_ext_max_value, 2, 1, 1, 1)

        self.el_ext_value = QLabel(self.el_ext_groupBox)
        self.el_ext_value.setObjectName(u"el_ext_value")
        self.el_ext_value.setFont(font2)
        self.el_ext_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.el_ext_value, 0, 0, 1, 2)

        self.el_ext_reset_pushButton = QPushButton(self.el_ext_groupBox)
        self.el_ext_reset_pushButton.setObjectName(u"el_ext_reset_pushButton")
        self.el_ext_reset_pushButton.setFont(font)

        self.gridLayout_3.addWidget(self.el_ext_reset_pushButton, 3, 0, 1, 2)


        self.horizontalLayout.addWidget(self.el_ext_groupBox)

        self.el_pro_groupBox = QGroupBox(self.tab1)
        self.el_pro_groupBox.setObjectName(u"el_pro_groupBox")
        self.el_pro_groupBox.setFont(font1)
        self.gridLayout_5 = QGridLayout(self.el_pro_groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.el_pro_max_label = QLabel(self.el_pro_groupBox)
        self.el_pro_max_label.setObjectName(u"el_pro_max_label")
        self.el_pro_max_label.setFont(font3)
        self.el_pro_max_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.el_pro_max_label, 2, 0, 1, 1)

        self.el_pro_value = QLabel(self.el_pro_groupBox)
        self.el_pro_value.setObjectName(u"el_pro_value")
        self.el_pro_value.setFont(font2)
        self.el_pro_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.el_pro_value, 0, 0, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 4, 0, 1, 1)

        self.el_pro_target_spinBox = QSpinBox(self.el_pro_groupBox)
        self.el_pro_target_spinBox.setObjectName(u"el_pro_target_spinBox")
        self.el_pro_target_spinBox.setFont(font)
        self.el_pro_target_spinBox.setMaximum(180)
        self.el_pro_target_spinBox.setSingleStep(10)
        self.el_pro_target_spinBox.setValue(150)

        self.gridLayout_5.addWidget(self.el_pro_target_spinBox, 5, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 1, 0, 1, 1)

        self.el_pro_reset_pushButton = QPushButton(self.el_pro_groupBox)
        self.el_pro_reset_pushButton.setObjectName(u"el_pro_reset_pushButton")
        self.el_pro_reset_pushButton.setFont(font)

        self.gridLayout_5.addWidget(self.el_pro_reset_pushButton, 3, 0, 1, 2)

        self.el_pro_target_label = QLabel(self.el_pro_groupBox)
        self.el_pro_target_label.setObjectName(u"el_pro_target_label")
        self.el_pro_target_label.setFont(font)
        self.el_pro_target_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.el_pro_target_label, 5, 0, 1, 1)

        self.el_pro_max_value = QLabel(self.el_pro_groupBox)
        self.el_pro_max_value.setObjectName(u"el_pro_max_value")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.el_pro_max_value.setPalette(palette2)
        self.el_pro_max_value.setFont(font3)

        self.gridLayout_5.addWidget(self.el_pro_max_value, 2, 1, 1, 1)


        self.horizontalLayout.addWidget(self.el_pro_groupBox)

        self.el_sup_groupBox = QGroupBox(self.tab1)
        self.el_sup_groupBox.setObjectName(u"el_sup_groupBox")
        self.el_sup_groupBox.setFont(font1)
        self.gridLayout_6 = QGridLayout(self.el_sup_groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_10, 1, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_9, 4, 0, 1, 1)

        self.el_sup_target_label = QLabel(self.el_sup_groupBox)
        self.el_sup_target_label.setObjectName(u"el_sup_target_label")
        self.el_sup_target_label.setFont(font)
        self.el_sup_target_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.el_sup_target_label, 5, 0, 1, 1)

        self.el_sup_value = QLabel(self.el_sup_groupBox)
        self.el_sup_value.setObjectName(u"el_sup_value")
        self.el_sup_value.setFont(font2)
        self.el_sup_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.el_sup_value, 0, 0, 1, 2)

        self.el_sup_reset_pushButton = QPushButton(self.el_sup_groupBox)
        self.el_sup_reset_pushButton.setObjectName(u"el_sup_reset_pushButton")
        self.el_sup_reset_pushButton.setFont(font)

        self.gridLayout_6.addWidget(self.el_sup_reset_pushButton, 3, 0, 1, 2)

        self.el_sup_max_label = QLabel(self.el_sup_groupBox)
        self.el_sup_max_label.setObjectName(u"el_sup_max_label")
        self.el_sup_max_label.setFont(font3)
        self.el_sup_max_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.el_sup_max_label, 2, 0, 1, 1)

        self.el_sup_target_spinBox = QSpinBox(self.el_sup_groupBox)
        self.el_sup_target_spinBox.setObjectName(u"el_sup_target_spinBox")
        self.el_sup_target_spinBox.setFont(font)
        self.el_sup_target_spinBox.setMaximum(180)
        self.el_sup_target_spinBox.setSingleStep(10)
        self.el_sup_target_spinBox.setValue(150)

        self.gridLayout_6.addWidget(self.el_sup_target_spinBox, 5, 1, 1, 1)

        self.el_sup_max_value = QLabel(self.el_sup_groupBox)
        self.el_sup_max_value.setObjectName(u"el_sup_max_value")
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.el_sup_max_value.setPalette(palette3)
        self.el_sup_max_value.setFont(font3)

        self.gridLayout_6.addWidget(self.el_sup_max_value, 2, 1, 1, 1)


        self.horizontalLayout.addWidget(self.el_sup_groupBox)

        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sh_flex_groupBox = QGroupBox(self.tab_2)
        self.sh_flex_groupBox.setObjectName(u"sh_flex_groupBox")
        self.sh_flex_groupBox.setFont(font1)
        self.gridLayout_12 = QGridLayout(self.sh_flex_groupBox)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.sh_flex_target_spinBox = QSpinBox(self.sh_flex_groupBox)
        self.sh_flex_target_spinBox.setObjectName(u"sh_flex_target_spinBox")
        self.sh_flex_target_spinBox.setFont(font)
        self.sh_flex_target_spinBox.setMaximum(180)
        self.sh_flex_target_spinBox.setSingleStep(10)
        self.sh_flex_target_spinBox.setValue(150)

        self.gridLayout_12.addWidget(self.sh_flex_target_spinBox, 5, 1, 1, 1)

        self.sh_flex_max_label = QLabel(self.sh_flex_groupBox)
        self.sh_flex_max_label.setObjectName(u"sh_flex_max_label")
        self.sh_flex_max_label.setFont(font3)
        self.sh_flex_max_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.sh_flex_max_label, 2, 0, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_22, 1, 0, 1, 1)

        self.sh_flex_target_label = QLabel(self.sh_flex_groupBox)
        self.sh_flex_target_label.setObjectName(u"sh_flex_target_label")
        self.sh_flex_target_label.setFont(font)
        self.sh_flex_target_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.sh_flex_target_label, 5, 0, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_21, 4, 0, 1, 1)

        self.sh_flex_reset_pushButton = QPushButton(self.sh_flex_groupBox)
        self.sh_flex_reset_pushButton.setObjectName(u"sh_flex_reset_pushButton")
        self.sh_flex_reset_pushButton.setFont(font)

        self.gridLayout_12.addWidget(self.sh_flex_reset_pushButton, 3, 0, 1, 2)

        self.sh_flex_value = QLabel(self.sh_flex_groupBox)
        self.sh_flex_value.setObjectName(u"sh_flex_value")
        self.sh_flex_value.setFont(font2)
        self.sh_flex_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.sh_flex_value, 0, 0, 1, 2)

        self.sh_flex_max_value = QLabel(self.sh_flex_groupBox)
        self.sh_flex_max_value.setObjectName(u"sh_flex_max_value")
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 128))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        self.sh_flex_max_value.setPalette(palette4)
        self.sh_flex_max_value.setFont(font3)

        self.gridLayout_12.addWidget(self.sh_flex_max_value, 2, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.sh_flex_groupBox)

        self.sh_abd_groupBox = QGroupBox(self.tab_2)
        self.sh_abd_groupBox.setObjectName(u"sh_abd_groupBox")
        self.sh_abd_groupBox.setFont(font1)
        self.gridLayout_10 = QGridLayout(self.sh_abd_groupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.sh_abd_target_label = QLabel(self.sh_abd_groupBox)
        self.sh_abd_target_label.setObjectName(u"sh_abd_target_label")
        self.sh_abd_target_label.setFont(font)
        self.sh_abd_target_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.sh_abd_target_label, 5, 0, 1, 1)

        self.sh_abd_reset_pushButton = QPushButton(self.sh_abd_groupBox)
        self.sh_abd_reset_pushButton.setObjectName(u"sh_abd_reset_pushButton")
        self.sh_abd_reset_pushButton.setFont(font)

        self.gridLayout_10.addWidget(self.sh_abd_reset_pushButton, 3, 0, 1, 2)

        self.sh_abd_max_value = QLabel(self.sh_abd_groupBox)
        self.sh_abd_max_value.setObjectName(u"sh_abd_max_value")
        palette5 = QPalette()
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.sh_abd_max_value.setPalette(palette5)
        self.sh_abd_max_value.setFont(font3)

        self.gridLayout_10.addWidget(self.sh_abd_max_value, 2, 1, 1, 1)

        self.sh_abd_target_spinBox = QSpinBox(self.sh_abd_groupBox)
        self.sh_abd_target_spinBox.setObjectName(u"sh_abd_target_spinBox")
        self.sh_abd_target_spinBox.setFont(font)
        self.sh_abd_target_spinBox.setMaximum(180)
        self.sh_abd_target_spinBox.setSingleStep(10)
        self.sh_abd_target_spinBox.setValue(150)

        self.gridLayout_10.addWidget(self.sh_abd_target_spinBox, 5, 1, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_17, 4, 0, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_18, 1, 0, 1, 1)

        self.sh_abd_max_label = QLabel(self.sh_abd_groupBox)
        self.sh_abd_max_label.setObjectName(u"sh_abd_max_label")
        self.sh_abd_max_label.setFont(font3)
        self.sh_abd_max_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.sh_abd_max_label, 2, 0, 1, 1)

        self.sh_abd_value = QLabel(self.sh_abd_groupBox)
        self.sh_abd_value.setObjectName(u"sh_abd_value")
        self.sh_abd_value.setFont(font2)
        self.sh_abd_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.sh_abd_value, 0, 0, 1, 2)


        self.horizontalLayout_2.addWidget(self.sh_abd_groupBox)

        self.sh_introt_groupBox = QGroupBox(self.tab_2)
        self.sh_introt_groupBox.setObjectName(u"sh_introt_groupBox")
        self.sh_introt_groupBox.setFont(font1)
        self.gridLayout_11 = QGridLayout(self.sh_introt_groupBox)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.sh_introt_max_value = QLabel(self.sh_introt_groupBox)
        self.sh_introt_max_value.setObjectName(u"sh_introt_max_value")
        palette6 = QPalette()
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.sh_introt_max_value.setPalette(palette6)
        self.sh_introt_max_value.setFont(font3)

        self.gridLayout_11.addWidget(self.sh_introt_max_value, 2, 1, 1, 1)

        self.sh_introt_target_label = QLabel(self.sh_introt_groupBox)
        self.sh_introt_target_label.setObjectName(u"sh_introt_target_label")
        self.sh_introt_target_label.setFont(font)
        self.sh_introt_target_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.sh_introt_target_label, 5, 0, 1, 1)

        self.sh_introt_target_spinBox = QSpinBox(self.sh_introt_groupBox)
        self.sh_introt_target_spinBox.setObjectName(u"sh_introt_target_spinBox")
        self.sh_introt_target_spinBox.setFont(font)
        self.sh_introt_target_spinBox.setMaximum(180)
        self.sh_introt_target_spinBox.setSingleStep(10)
        self.sh_introt_target_spinBox.setValue(150)

        self.gridLayout_11.addWidget(self.sh_introt_target_spinBox, 5, 1, 1, 1)

        self.sh_introt_reset_pushButton = QPushButton(self.sh_introt_groupBox)
        self.sh_introt_reset_pushButton.setObjectName(u"sh_introt_reset_pushButton")
        self.sh_introt_reset_pushButton.setFont(font)

        self.gridLayout_11.addWidget(self.sh_introt_reset_pushButton, 3, 0, 1, 2)

        self.sh_introt_max_label = QLabel(self.sh_introt_groupBox)
        self.sh_introt_max_label.setObjectName(u"sh_introt_max_label")
        self.sh_introt_max_label.setFont(font3)
        self.sh_introt_max_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.sh_introt_max_label, 2, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_19, 4, 0, 1, 1)

        self.sh_introt_value = QLabel(self.sh_introt_groupBox)
        self.sh_introt_value.setObjectName(u"sh_introt_value")
        self.sh_introt_value.setFont(font2)
        self.sh_introt_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.sh_introt_value, 0, 0, 1, 2)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_20, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.sh_introt_groupBox)

        self.sh_extrot_groupBox = QGroupBox(self.tab_2)
        self.sh_extrot_groupBox.setObjectName(u"sh_extrot_groupBox")
        self.sh_extrot_groupBox.setFont(font1)
        self.gridLayout_13 = QGridLayout(self.sh_extrot_groupBox)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_24, 1, 0, 1, 1)

        self.sh_extrot_max_label = QLabel(self.sh_extrot_groupBox)
        self.sh_extrot_max_label.setObjectName(u"sh_extrot_max_label")
        self.sh_extrot_max_label.setFont(font3)
        self.sh_extrot_max_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.sh_extrot_max_label, 2, 0, 1, 1)

        self.sh_extrot_value = QLabel(self.sh_extrot_groupBox)
        self.sh_extrot_value.setObjectName(u"sh_extrot_value")
        self.sh_extrot_value.setFont(font2)
        self.sh_extrot_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.sh_extrot_value, 0, 0, 1, 2)

        self.sh_extrot_target_spinBox = QSpinBox(self.sh_extrot_groupBox)
        self.sh_extrot_target_spinBox.setObjectName(u"sh_extrot_target_spinBox")
        self.sh_extrot_target_spinBox.setFont(font)
        self.sh_extrot_target_spinBox.setMaximum(180)
        self.sh_extrot_target_spinBox.setSingleStep(10)
        self.sh_extrot_target_spinBox.setValue(150)

        self.gridLayout_13.addWidget(self.sh_extrot_target_spinBox, 5, 1, 1, 1)

        self.sh_extrot_target_label = QLabel(self.sh_extrot_groupBox)
        self.sh_extrot_target_label.setObjectName(u"sh_extrot_target_label")
        self.sh_extrot_target_label.setFont(font)
        self.sh_extrot_target_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.sh_extrot_target_label, 5, 0, 1, 1)

        self.sh_extrot_reset_pushButton = QPushButton(self.sh_extrot_groupBox)
        self.sh_extrot_reset_pushButton.setObjectName(u"sh_extrot_reset_pushButton")
        self.sh_extrot_reset_pushButton.setFont(font)

        self.gridLayout_13.addWidget(self.sh_extrot_reset_pushButton, 3, 0, 1, 2)

        self.sh_extrot_max_value = QLabel(self.sh_extrot_groupBox)
        self.sh_extrot_max_value.setObjectName(u"sh_extrot_max_value")
        palette7 = QPalette()
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.sh_extrot_max_value.setPalette(palette7)
        self.sh_extrot_max_value.setFont(font3)

        self.gridLayout_13.addWidget(self.sh_extrot_max_value, 2, 1, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_23, 4, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.sh_extrot_groupBox)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(LiveWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(LiveWindow)
    # setupUi

    def retranslateUi(self, LiveWindow):
        LiveWindow.setWindowTitle(QCoreApplication.translate("LiveWindow", u"Form", None))
        self.el_flex_groupBox.setTitle(QCoreApplication.translate("LiveWindow", u"Flexion", None))
        self.el_flex_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.el_flex_reset_pushButton.setText(QCoreApplication.translate("LiveWindow", u"Reset", None))
        self.el_flex_max_value.setText(QCoreApplication.translate("LiveWindow", u"MaxVal", None))
        self.el_flex_target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.el_flex_max_label.setText(QCoreApplication.translate("LiveWindow", u"Max achieved:", None))
        self.el_ext_groupBox.setTitle(QCoreApplication.translate("LiveWindow", u"Extension", None))
        self.el_ext_target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.el_ext_max_label.setText(QCoreApplication.translate("LiveWindow", u"Min achieved:", None))
        self.el_ext_max_value.setText(QCoreApplication.translate("LiveWindow", u"MaxVal", None))
        self.el_ext_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.el_ext_reset_pushButton.setText(QCoreApplication.translate("LiveWindow", u"Reset", None))
        self.el_pro_groupBox.setTitle(QCoreApplication.translate("LiveWindow", u"Pronation", None))
        self.el_pro_max_label.setText(QCoreApplication.translate("LiveWindow", u"Max achieved:", None))
        self.el_pro_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.el_pro_reset_pushButton.setText(QCoreApplication.translate("LiveWindow", u"Reset", None))
        self.el_pro_target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.el_pro_max_value.setText(QCoreApplication.translate("LiveWindow", u"MaxVal", None))
        self.el_sup_groupBox.setTitle(QCoreApplication.translate("LiveWindow", u"Supination", None))
        self.el_sup_target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.el_sup_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.el_sup_reset_pushButton.setText(QCoreApplication.translate("LiveWindow", u"Reset", None))
        self.el_sup_max_label.setText(QCoreApplication.translate("LiveWindow", u"Max achieved:", None))
        self.el_sup_max_value.setText(QCoreApplication.translate("LiveWindow", u"MaxVal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("LiveWindow", u"Elbow", None))
        self.sh_flex_groupBox.setTitle(QCoreApplication.translate("LiveWindow", u"Flexion", None))
        self.sh_flex_max_label.setText(QCoreApplication.translate("LiveWindow", u"Max achieved:", None))
        self.sh_flex_target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.sh_flex_reset_pushButton.setText(QCoreApplication.translate("LiveWindow", u"Reset", None))
        self.sh_flex_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.sh_flex_max_value.setText(QCoreApplication.translate("LiveWindow", u"MaxVal", None))
        self.sh_abd_groupBox.setTitle(QCoreApplication.translate("LiveWindow", u"Abduction", None))
        self.sh_abd_target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.sh_abd_reset_pushButton.setText(QCoreApplication.translate("LiveWindow", u"Reset", None))
        self.sh_abd_max_value.setText(QCoreApplication.translate("LiveWindow", u"MaxVal", None))
        self.sh_abd_max_label.setText(QCoreApplication.translate("LiveWindow", u"Max achieved:", None))
        self.sh_abd_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.sh_introt_groupBox.setTitle(QCoreApplication.translate("LiveWindow", u"Internal Rotation", None))
        self.sh_introt_max_value.setText(QCoreApplication.translate("LiveWindow", u"MaxVal", None))
        self.sh_introt_target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.sh_introt_reset_pushButton.setText(QCoreApplication.translate("LiveWindow", u"Reset", None))
        self.sh_introt_max_label.setText(QCoreApplication.translate("LiveWindow", u"Max achieved:", None))
        self.sh_introt_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.sh_extrot_groupBox.setTitle(QCoreApplication.translate("LiveWindow", u"External Rotation", None))
        self.sh_extrot_max_label.setText(QCoreApplication.translate("LiveWindow", u"Max achieved:", None))
        self.sh_extrot_value.setText(QCoreApplication.translate("LiveWindow", u"Current Value", None))
        self.sh_extrot_target_label.setText(QCoreApplication.translate("LiveWindow", u"Target:", None))
        self.sh_extrot_reset_pushButton.setText(QCoreApplication.translate("LiveWindow", u"Reset", None))
        self.sh_extrot_max_value.setText(QCoreApplication.translate("LiveWindow", u"MaxVal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("LiveWindow", u"Shoulder", None))
    # retranslateUi

