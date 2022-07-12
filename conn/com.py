#!/bin/env python3
# -*- coding: utf-8 -*-
# author: ziu andiest
# email:andiest13@gmail.com

import time
import serial
import utils
import serial.tools.list_ports
from enum import Enum


class ConnectionStatus(Enum):
    CLOSED = 0
    CONNECTED = 1
    LOSE = 2
    CONNECTING = 3


class DcSerial:
    def __init__(self) -> None:
        self.isOpened = False
        self.busy = False
        self.status = ConnectionStatus.CLOSED
        self.isDetectSerialPort = False
        self.com = serial.Serial()

    def connect(self, port):
        if self.com.is_open:
            self.com.close()
        self.com.port = port
        self.com.baudrate = 9600
        self.com.timeout = 0
        self.com.parity = serial.PARITY_EVEN
        self.com.rtscts = 1
        self.com.open()
        return self.com.is_open

    def send(self, string):
        # 格式化发送指令
        data = self.parseSendData(data=string, encoding="ASCII", isHexStr=True)
        self.com.write(data)
        # 处理返回
        time.sleep(0.5)
        length = max(1, self.com.in_waiting)
        data = self.com.read(length)
        # print(data)
        return utils.bytes_to_hex_str(data)

    def disconnect(self):
        if self.com.is_open:
            self.com.close()
        return self.com.is_open

    # def read(self):
    #     while self.com.is_open:
    #         length = max(1, self.com.in_waiting)
    #         data = self.com.read(length)
    #         print(data)
    #         time.sleep(1)

    def __del__(self):
        try:
            self.com.close()
        except Exception:
            pass

    def parseSendData(self, data: str, encoding, usrCRLF=False, isHexStr=False, escape=False):
        if not data:
            return b''
        if usrCRLF:
            data = data.replace("\n", "\r\n")
        if isHexStr:
            if usrCRLF:
                data = data.replace("\r\n", " ")
            else:
                data = data.replace("\n", " ")
            data = utils.hex_str_to_bytes(data)
            if data == -1:
                # self.hintSignal.emit("error", _("Error"), _("Format error, should be like 00 01 02 03"))
                return b''
        else:
            if not escape:
                data = data.encode(encoding, "ignore")
            else:
                try:
                    data = utils.str_to_bytes(data, escape=True, encoding=encoding)
                except Exception:
                    # self.hintSignal.emit("error", _("Error"), _("Escape is on, but escape error:") + str(e))
                    return b''
        return data
