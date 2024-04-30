def main(data):
    number = int(data)
    shifts = {'K1': (0, 8), 'K2': (8, 11), 'K3': (11, 15), 'K4': (15, 25),
              'K6': (30, 39)}
    result = []
    for field, (start, end) in shifts.items():
        mask = (1 << (end - start)) - 1
        value = (number >> start) & mask
        result.append((field, value))
    return result
