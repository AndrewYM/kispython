from math import ceil


def main(y):
    return 8*y-3*(65*y*y)**3 if y < 57 else ceil(22*y*y)/15 \
        if 57 <= y < 115 else 49*y**7
