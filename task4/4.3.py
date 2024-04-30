import math


def main(n):
    arr = [-0.79]
    for i in range(1, n + 1):
        arr.append(arr[-1] / 80 - math.ceil(arr[-1]) ** 2)
    return arr[-1]
