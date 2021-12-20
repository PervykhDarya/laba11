import math

def cylinder():
    try:
        r = float(input())
        h = float(input())
    except valueError:
        return

    side = 2 * math.pi * r * h
    circle = math.pi * r ** 2
    full = side + 2 * circle
    return full

print(cylinder())