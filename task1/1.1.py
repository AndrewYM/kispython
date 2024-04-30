import math


def main(x, z):
    a = ((z * z - x)**4 - 94 * (z * z + 71 + x**3)**5)
    b = (z * z + 35 * (26 * x**3)**5)
    c = 44 * (z + z * z + z**3)**7 + x
    y = a / b + c
    return y
