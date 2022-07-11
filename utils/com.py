#!/bin/env python3
# -*- coding: utf-8 -*-
# author: ziu andiest
# email:andiest13@gmail.com

import serial
import serial.tools.list_ports


class DcSerial:
    def __init__(self, data: list):
        self.data = data

    @classmethod
    def listComPorts(cls):
        data = []
        ports = list(serial.tools.list_ports.comports())

        for port_ in ports:
            obj = Object(data=dict({"device": port_.device, "description": port_.description.split("(")[0].strip()}))
            data.append(obj)
        return cls(data=data)


class Object:
    def __init__(self, data: dict):
        self.data = data
        self.device = data.get("device")
        self.description = data.get("description")


if __name__ == '__main__':
    for port in DcSerial.listComPorts().data:
        print(port.device)
        print(port.description)

# ser = serial.Serial('COM3', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
# ser.open()
# if ser.is_open:
#     command = 'FAFD0100DF'
#     ser.write(command.decode('hex'))
#     ser.close()