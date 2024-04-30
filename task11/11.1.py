class MealyError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Mealy:
    def __init__(self):
        self.state = 'A'

    def sit(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'E'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'E'
            return 8
        if self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError('sit')

    def coat(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError('coat')

    def tail(self):
        if self.state == 'D':
            self.state = 'A'
            return 6
        if self.state == 'B':
            self.state = 'F'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 4
        else:
            raise MealyError('tail')


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
