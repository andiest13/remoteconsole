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
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_open = QPushButton(self.centralwidget)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setGeometry(QRect(20, 300, 51, 31))
        self.btn_study = QPushButton(self.centralwidget)
        self.btn_study.setObjectName(u"btn_study")
        self.btn_study.setGeometry(QRect(280, 500, 100, 32))
        self.ports_list = QComboBox(self.centralwidget)
        self.ports_list.setObjectName(u"ports_list")
        self.ports_list.setGeometry(QRect(10, 10, 371, 31))
        self.btn_switch = QPushButton(self.centralwidget)
        self.btn_switch.setObjectName(u"btn_switch")
        self.btn_switch.setGeometry(QRect(20, 40, 100, 32))
        self.txt_result = QTextEdit(self.centralwidget)
        self.txt_result.setObjectName(u"txt_result")
        self.txt_result.setGeometry(QRect(20, 70, 361, 211))
        self.txt_result.setReadOnly(True)
        self.btn_debug = QPushButton(self.centralwidget)
        self.btn_debug.setObjectName(u"btn_debug")
        self.btn_debug.setGeometry(QRect(260, 370, 100, 40))
        self.txt_text = QTextEdit(self.centralwidget)
        self.txt_text.setObjectName(u"txt_text")
        self.txt_text.setGeometry(QRect(20, 380, 231, 31))
        self.btn_close = QPushButton(self.centralwidget)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(170, 500, 100, 32))
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
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u673a", None))
        self.btn_study.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u4e60", None))
        self.btn_switch.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.btn_debug.setText(QCoreApplication.translate("MainWindow", u"\u8c03\u8bd5", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u673a", None))
    # retranslateUi

