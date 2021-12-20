# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def test():
    a = int(input("Введите число: "))
    if 0 < a:
        positive(a)
    elif a == 0:
        print("Это не положительное и не отрицательное число")
    else:
        negative(a)

def positive(a):
    print("Это положительное число")

def negative(a):
    print("Это отрицательное число")

if __name__ == '__main__':
    test()