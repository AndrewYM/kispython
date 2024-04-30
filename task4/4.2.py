import math


def main(n):
    res = -0.79
    for i in range(n):
        res = res / 80 - math.ceil(res) ** 2
    return res
