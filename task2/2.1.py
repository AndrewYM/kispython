import math


def main(y):
    if y < 57:
        return 8*y-3*(65*y*y)**3
    if 57 <= y < 115:
        return math.ceil(22*y*y)/15
    if y >= 115:
        return 49*y**7
