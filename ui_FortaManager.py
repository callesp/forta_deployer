# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FortaManagerjAlEyq.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(716, 590)
        MainWindow.setStyleSheet(u".QFrame{\n"
"	background-color: rgb(213, 213, 213);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(120, 0))
        self.frame.setStyleSheet(u".QFrame{\n"
"	background-color: rgb(159, 159, 159);\n"
"}\n"
"\n"
".QPushButton{\n"
"	color: rgb(40, 40, 40);\n"
"	background-color: rgb(171, 171, 171);\n"
"	border-radius: 0px;\n"
"	height: 30;\n"
"	padding: 5px;\n"
"	border-left: 5px solid transparent;\n"
"}\n"
"\n"
".QPushButton[on=true]{\n"
"	background-color: rgb(8, 98, 182);\n"
"}\n"
"\n"
".QPushButton[on=false]{\n"
"	background-color: rgb(171, 171, 171);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(158, 158, 158);\n"
"	border-left: 5px solid rgb(5, 11, 34);\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_main = QPushButton(self.frame)
        self.pushButton_main.setObjectName(u"pushButton_main")
        self.pushButton_main.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_main)

        self.pushButton_database = QPushButton(self.frame)
        self.pushButton_database.setObjectName(u"pushButton_database")

        self.verticalLayout.addWidget(self.pushButton_database)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_main.setText(QCoreApplication.translate("MainWindow", u"Main", None))
        self.pushButton_database.setText(QCoreApplication.translate("MainWindow", u"DataBase", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Opt1", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Opt2", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Opt3", None))
    # retranslateUi

