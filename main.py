#!/bin/env python3
# -*- coding: utf-8 -*-
# author: ziu andiest
# email:andiest13@gmail.com

import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

from conn import com_ports
from conn.com import DcSerial


class RcWindow(object):
    def __init__(self):
        loader = QUiLoader()
        self.dialog = loader.load("remoteconsole.ui", None)
        self.dialog.show()
        for port in com_ports.serial_ports():
            self.dialog.ports_list.addItem(port)
        self.com = DcSerial()
        self.btn_event()
        self.is_open = False

    # 按钮事件绑定
    def btn_event(self):
        self.dialog.btn_study.clicked.connect(lambda: self.btn_study())
        self.dialog.btn_switch.clicked.connect(lambda: self.btn_switch_click())
        self.dialog.btn_open.clicked.connect(lambda: self.open_dev())
        self.dialog.btn_test.clicked.connect(lambda: self.test())
        # self.dialog.txt_result.insertPlainText

    # 点击连接com口
    def btn_switch_click(self):
        com_port = self.dialog.ports_list.currentText()
        if not self.is_open:
            self.dialog.btn_switch.setText("关闭")
            self.is_open = True
            return_data = self.com.connect(com_port)
            if return_data:
                self.dialog.txt_result.insertPlainText('成功打开com串口:' + str(return_data) + '\n')
        else:
            self.com.disconnect()
            self.dialog.btn_switch.setText("打开")
            self.is_open = False
            self.dialog.txt_result.insertPlainText('已关闭串口\n')

    # def receive(self):
    #     while self.is_open:
    #         try:
    #             length = max(1, self.com.)

    def send_data(self, string):
        self.dialog.txt_result.insertPlainText('=>' + string + '\n')
        return_data = self.com.send(string)
        self.dialog.txt_result.insertPlainText('<=' + return_data + '\n')

    # 发送学习指令
    def btn_study(self):
        string = 'FA FD 01 01 DF'
        self.send_data(string)

    def open_dev(self):
        string = 'FA FD 02 01 DF'
        self.send_data(string)

    def test(self):
        string = self.dialog.txt_text.toPlainText()
        # print(string)
        # string = 'FA FD 06 00 DF'
        self.send_data(string)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RcWindow()
    app.exec()
