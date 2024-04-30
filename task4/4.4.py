import math


def main(n):
    match n:
        case 0:
            return -0.79
        case _:
            return main(n-1)/80-math.ceil(main(n-1))**2
