from struct import *


def parse_data(buf, offset, fmt, order='>'):
    d = {
        'float': 'f',
        'double': 'd',
        'char': 'c',
        'int8': 'b',
        'uint8': 'B',
        'int16': 'h',
        'uint16': 'H',
        'int32': 'i',
        'uint32': 'I',
        'int64': 'q',
        'uint64': 'Q'
    }[fmt]
    size = calcsize(order + d)
    result = unpack_from(order + d, buf, offset)[0]
    return result, offset + size


def parse_d(buf, offset):
    d1 = []
    for _ in range(7):
        value, offset = parse_data(buf, offset, 'uint16')
        d1.append(value)
    d2, offset = parse_data(buf, offset, 'uint8')
    d3_size, offset = parse_data(buf, offset, 'uint16')
    d3_offset, offset = parse_data(buf, offset, 'uint32')
    d3 = [parse_data(buf, d3_offset + i, 'int8')[0] for i in range(d3_size)]
    d4, offset = parse_data(buf, offset, 'uint16')
    d5, offset = parse_data(buf, offset, 'uint8')
    d6 = [parse_data(buf, offset + i * 2, 'uint16')[0] for i in range(7)]
    offset += 7 * 2
    d7, offset = parse_data(buf, offset, 'uint64')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4, 'D5': d5, 'D6': d6,
            'D7': d7}, offset


def parse_c(buf, offset):
    c1, offset = parse_data(buf, offset, 'uint8')
    c2, offset = parse_data(buf, offset, 'int8')
    c3, offset = parse_data(buf, offset, 'int16')
    c4, offset = parse_d(buf, offset)
    c5, offset = parse_data(buf, offset, 'float')
    c6, offset = parse_data(buf, offset, 'uint64')
    c7, offset = parse_data(buf, offset, 'float')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4, 'C5': c5, 'C6': c6,
            'C7': c7}, offset


def parse_b(buf, offset):
    b1, offset = parse_data(buf, offset, 'int16')
    b2, offset = parse_data(buf, offset, 'uint32')
    return {'B1': b1, 'B2': b2}, offset


def parse_a(buf, offset):
    a1, offset = parse_data(buf, offset, 'uint16')
    a2 = []
    for _ in range(3):
        b, offset = parse_b(buf, offset)
        a2.append(b)
    a3 = buf[offset:offset+2].decode('ascii')
    offset += 2
    a4_offset, offset = parse_data(buf, offset, 'uint16')
    a4, _ = parse_c(buf, a4_offset)
    a5, offset = parse_data(buf, offset, 'int32')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5}, offset


def main(data):
    offset = 4
    return parse_a(data, offset)[0]
