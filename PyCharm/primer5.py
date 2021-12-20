import math
import sys

figure = input("1-прямоугольник, 2-треугольник, 3-круг: ")

if figure == '1':
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    print(f"Площадь: {a * b}")
elif figure == '2':
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    print(f"Площадь: {0.5 * a * h}")
elif figure == '3':
    r = float(input("Радиус: "))
    print(f"Площадь: {math.pi * r**2}")
else:
    print("Ошибка ввода", file=sys.stderr)