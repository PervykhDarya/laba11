import math

def cylinder(h, r=1):
    side = 2 * math.pi * r * h
    circle = math.pi * r ** 2
    full = side + 2 * circle
    return full

figure1 = cylinder(4, 3)
figure2 = cylinder(5)
print(figure1)
print(figure2)