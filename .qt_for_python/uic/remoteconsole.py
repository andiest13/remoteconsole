# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remoteconsole.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 100, 361, 101))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 359, 99))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 230, 100, 32))
        self.btn_study = QPushButton(self.centralwidget)
        self.btn_study.setObjectName(u"btn_study")
        self.btn_study.setGeometry(QRect(280, 500, 100, 32))
        self.ports_list = QComboBox(self.centralwidget)
        self.ports_list.setObjectName(u"ports_list")
        self.ports_list.setGeometry(QRect(10, 10, 371, 31))
        self.btn_switch = QPushButton(self.centralwidget)
        self.btn_switch.setObjectName(u"btn_switch")
        self.btn_switch.setGeometry(QRect(20, 40, 100, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u683c\u529b\u7a7a\u8c03\u9065\u63a7", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u5173", None))
        self.btn_study.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u4e60", None))
        self.btn_switch.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
    # retranslateUi

