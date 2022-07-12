#!/bin/env python3
# -*- coding: utf-8 -*-
# author: ziu andiest
# email:andiest13@gmail.com


class Gree:
    """
    格力空调类
    """

    KEY_ON = 1
    KEY_OFF = 0

    MODE_AUTO = 0  # 自动
    MODE_REFRIGERATION = 1  # 制冷
    MODE_HEATING = 4  # 制热

    @staticmethod
    def _little_bit(num, digits):
        s = f'{num:0{digits}b}'[-digits:][::-1]
        return [int(b) for b in s]

    @staticmethod
    def create_ir_data(key: int, mode: int, temp: int):
        return Gree._create_ir_data(key=key, mode=mode, temp=temp)

    @staticmethod
    def _create_ir_data(**kwargs):
        mode = kwargs.get('mode', 0)  # 模式
        key = kwargs.get('key', 0)  # 开关 0,1
        temp = kwargs.get('temp', 24) - 16  # 温度
        verify = mode + temp - key * 8 + 10
        # 不校验数据合法性
        ir_data = [[[], []], [[], []]]
        ir_data[0][0] = Gree._little_bit(mode, 3)  # 模式
        ir_data[0][0] += Gree._little_bit(key, 1)  # 开关
        ir_data[0][0] += Gree._little_bit(0, 4)
        ir_data[0][0] += Gree._little_bit(temp, 4)  # 温度
        ir_data[0][0] += [0, 0, 0, 0, 0, 0, 0, 0, 0,
                          1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0]
        ir_data[0][1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ir_data[0][1] += Gree._little_bit(verify, 4)  # 校验位
        ir_data[1][0] = ir_data[0][0].copy()
        ir_data[1][1] = ir_data[0][1].copy()
        ir_data[1][0][29] = 1
        return ir_data


def main():
    ir_data = Gree.create_ir_data(key=Gree.KEY_ON, mode=Gree.MODE_REFRIGERATION, temp=16)
    print(ir_data[0])


if __name__ == '__main__':
    main()
