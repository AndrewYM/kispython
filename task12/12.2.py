import struct


def parse_data(buf, offset, fmt):
    result = struct.unpack_from(fmt, buf, offset)
    return result[0], offset + struct.calcsize(fmt)


def parse_d(buf, offset):
    d1 = []
    for _ in range(7):
        value, offset = parse_data(buf, offset, '>H')
        d1.append(value)
    d2, offset = parse_data(buf, offset, '>B')
    d3_size, offset = parse_data(buf, offset, '>H')
    d3_offset, offset = parse_data(buf, offset, '>I')
    d3 = [parse_data(buf, d3_offset + i, '>b')[0] for i in range(d3_size)]
    d4, offset = parse_data(buf, offset, '>H')
    d5, offset = parse_data(buf, offset, '>B')
    d6 = [parse_data(buf, offset + i * 2, '>H')[0] for i in range(7)]
    offset += 7 * 2
    d7, offset = parse_data(buf, offset, '>Q')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4, 'D5': d5, 'D6': d6,
            'D7': d7}, offset


def parse_c(buf, offset):
    c1, offset = parse_data(buf, offset, '>B')
    c2, offset = parse_data(buf, offset, '>b')
    c3, offset = parse_data(buf, offset, '>h')
    c4, offset = parse_d(buf, offset)
    c5, offset = parse_data(buf, offset, '>f')
    c6, offset = parse_data(buf, offset, '>Q')
    c7, offset = parse_data(buf, offset, '>f')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4, 'C5': c5, 'C6': c6,
            'C7': c7}, offset


def parse_b(buf, offset):
    b1, offset = parse_data(buf, offset, '>h')
    b2, offset = parse_data(buf, offset, '>I')
    return {'B1': b1, 'B2': b2}, offset


def parse_a(buf, offset):
    a1, offset = parse_data(buf, offset, '>H')
    a2 = []
    for _ in range(3):
        b, offset = parse_b(buf, offset)
        a2.append(b)
    a3, offset = parse_data(buf, offset, '>2s')
    a3 = a3.decode()
    a4_offset, offset = parse_data(buf, offset, '>H')
    a4, _ = parse_c(buf, a4_offset)
    a5, offset = parse_data(buf, offset, '>i')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5}, offset


def main(data):
    offset = 4
    return parse_a(data, offset)[0]
