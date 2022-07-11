#!/bin/env python3
# -*- coding: utf-8 -*-
# author: ziu andiest
# email:andiest13@gmail.com

import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

from utils import com_ports


class RcWindow(object):
    def __init__(self):
        loader = QUiLoader()
        self.dialog = loader.load("remoteconsole.ui", None)
        for port in com_ports.serial_ports():
            self.dialog.ports_list.addItem(port)
        self.btn_event()
        self.is_open = 0

    def btn_event(self):
        self.dialog.btn_study.clicked.connect(lambda: print("clicked"))
        self.dialog.btn_switch.clicked.connect(lambda: self.btn_switch_click())

    def btn_switch_click(self):
        com_port = self.dialog.ports_list.currentText()
        if self.is_open == 0:
            self.dialog.btn_switch.setText("关闭")
            self.is_open = 1
            print(com_port)
        elif self.is_open == 1:
            self.dialog.btn_switch.setText("打开")
            self.is_open = 0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RcWindow()
    window.dialog.show()
    sys.exit(app.exec_())

    # loader = QUiLoader()
    # app = QtWidgets.QApplication(sys.argv)
    # window = loader.load("remoteconsole.ui", None)
    # for port in com_ports.serial_ports():
    #     window.ports_list.addItem(port)
    # is_open = 0
    # window.btn_switch.clicked.connect()

    # window.btn_study.clicked.connect(lambda: print("clicked"))
    # window.show()
    # sys.exit(app.exec_())