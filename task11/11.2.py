class MealyError(Exception):
    def init(self, message):
        super().init(message)


class Mealy:
    def init(self):
        self.state = 'A'

    def sit(self):
        match self.state:
            case 'A':
                self.state = 'B'
                return 0
            case 'B':
                self.state = 'E'
                return 3
            case 'D':
                self.state = 'E'
                return 5
            case 'E':
                self.state = 'E'
                return 8
            case 'F':
                self.state = 'G'
                return 9
            case _:
                raise MealyError('sit')

    def tail(self):
        match self.state:
            case 'B':
                self.state = 'F'
                return 2
            case 'C':
                self.state = 'D'
                return 4
            case 'D':
                self.state = 'A'
                return 6
            case _:
                raise MealyError('tail')

    def coat(self):
        match self.state:
            case 'B':
                self.state = 'C'
                return 1
            case 'E':
                self.state = 'F'
                return 7
            case _:
                raise MealyError('coat')


def test():
    o = main()

    assert o.sit() == 0
    o.state = 'B'
    assert o.sit() == 3
    o.state = 'D'
    assert o.sit() == 5
    o.state = 'E'
    assert o.sit() == 8
    o.state = 'F'
    assert o.sit() == 9
    o.state = 'G'
    try:
        o.sit()
    except MealyError:
        pass

    o.state = 'B'
    assert o.coat() == 1
    o.state = 'E'
    assert o.coat() == 7
    o.state = 'D'
    try:
        o.coat()
    except MealyError:
        pass

    o.state = 'D'
    assert o.tail() == 6
    o.state = 'B'
    assert o.tail() == 2
    o.state = 'C'
    assert o.tail() == 4
    o.state = 'E'
    try:
        o.tail()
    except MealyError:
        pass

    o.state = 'A'
    assert o.sit() == 0
    assert o.coat() == 1
    assert o.tail() == 4
    assert o.tail() == 6
    assert o.sit() == 0
    assert o.coat() == 1
    assert o.tail() == 4
    assert o.sit() == 5
    assert o.sit() == 8
    assert o.sit() == 8
    assert o.coat() == 7
    assert o.sit() == 9

    o = main()
    try:
        o.coat()
    except MealyError:
        pass

    o = main()
    try:
        o.tail()
    except MealyError:
        pass


def main():
    return Mealy()


test()
