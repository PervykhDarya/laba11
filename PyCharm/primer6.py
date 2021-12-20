import math
import sys

figure = input("1-прямоугольник, 2-треугольник, 3-круг: ")

def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    print(f"Площадь: {a * b}")


def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    print(f"Площадь: {0.5 * a * h}")


def circle():
    r = float(input("Радиус: "))
    print(f"Площадь: {math.pi * r ** 2}")


if figure == '1':
    rectangle()
elif figure == '2':
    triangle()
elif figure == '3':
    circle()
else:
    print("Ошибка ввода", file=sys.stderr)