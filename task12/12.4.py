import struct


class Parser:
    d = {
        'float': '<f',
        'double': '<d',
        'char': '<c',
        'int8': '<b',
        'uint8': '<B',
        'int16': '<h',
        'uint16': '<H',
        'int32': '<i',
        'uint32': '<I',
        'int64': '<q',
        'uint64': '<Q'
    }

    def __init__(self, buf, offset):
        self.buf = buf
        self.offset = offset

    def join(self, offset):
        return Parser(self.buf, offset)

    def get(self, fmt):
        result = struct.unpack_from(fmt, self.buf, self.offset)
        self.offset += struct.calcsize(fmt)
        return result[0]


def parse_d(parser):
    d1 = [parser.get('>H') for _ in range(7)]
    d2 = parser.get('>B')
    d3_size = parser.get('>H')
    d3_offset = parser.get('>I')
    d3_parser = parser.join(d3_offset)
    d3 = [d3_parser.get('>b') for _ in range(d3_size)]
    d4 = parser.get('>H')
    d5 = parser.get('>B')
    d6 = [parser.get('>H') for _ in range(7)]
    d7 = parser.get('>Q')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4, 'D5': d5, 'D6': d6,
            'D7': d7}


def parse_c(parser):
    c1 = parser.get('>B')
    c2 = parser.get('>b')
    c3 = parser.get('>h')
    c4 = parse_d(parser)
    c5 = parser.get('>f')
    c6 = parser.get('>Q')
    c7 = parser.get('>f')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4, 'C5': c5, 'C6': c6,
            'C7': c7}


def parse_b(parser):
    b1 = parser.get('>h')
    b2 = parser.get('>I')
    return {'B1': b1, 'B2': b2}


def parse_a(parser):
    a1 = parser.get('>H')
    a2 = [parse_b(parser) for _ in range(3)]
    a3 = parser.get('>2s').decode()
    a4_offset = parser.get('>H')
    a4 = parse_c(parser.join(a4_offset))
    a5 = parser.get('>i')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5}


def main(data):
    parser = Parser(data, 4)
    return parse_a(parser)
