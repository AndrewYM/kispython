import math


def main(n):
    if (n == 0):
        return -0.79
    else:
        return main(n-1)/80-math.ceil(main(n-1))**2
