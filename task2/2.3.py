from math import ceil


def main(y):
    conditions = {
        y < 57: lambda y: 8*y-3*(65*y*y)**3,
        57 <= y < 115: lambda y: ceil(22*y*y)/15,
        y > 115: lambda y: 49*y**7,
    }
    return conditions[True](y)
