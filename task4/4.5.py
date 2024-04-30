import math


def main(n):
    return -0.79 if n == 0 else main(n-1)/80-math.ceil(main(n-1))**2
