def main(data):
    number = int(data)
    k1 = (number >> 0) & ((1 << 8) - 1)
    k2 = (number >> 8) & ((1 << 3) - 1)
    k3 = (number >> 11) & ((1 << 4) - 1)
    k4 = (number >> 15) & ((1 << 10) - 1)
    k6 = (number >> 30) & ((1 << 9) - 1)
    return [('K1', k1), ('K2', k2), ('K3', k3), ('K4', k4), ('K6', k6)]
