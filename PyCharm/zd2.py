# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

def cylinder():
    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))

    def circle():
        plk = math.pi * r ** 2
        return plk

    numbers = input("1 - площадь боковой поверхности, 2 - полная площадь: ")
    if numbers == '1':
        print(2 * math.pi * r * h)
    elif numbers == '2':
        print(circle()*2)
    else:
        print("Ошибка")

if __name__ == '__main__':
    cylinder()