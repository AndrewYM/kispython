import math


def main(x, z):
    return ((z * z - x) ** 4 - 94 * (z * z + 71 + x ** 3) ** 5) / \
        (z * z + 35 * (26 * x ** 3) ** 5) + \
        44 * (z + z * z + z ** 3) ** 7 + x
