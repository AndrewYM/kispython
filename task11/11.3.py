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
    test_exceptions = [
        ('A', 'coat'),
        ('A', 'tail'),
        ('C', 'sit'),
        ('C', 'coat'),
        ('D', 'coat'),
        ('E', 'tail'),
        ('F', 'coat'),
        ('F', 'tail'),
        ('G', 'sit'),
        ('G', 'coat'),
        ('G', 'tail'),
    ]
    test_result = [
        ('A', 'sit', 0, 'B'),
        ('B', 'coat', 1, 'C'),
        ('B', 'tail', 2, 'F'),
        ('B', 'sit', 3, 'E'),
        ('C', 'tail', 4, 'D'),
        ('D', 'sit', 5, 'E'),
        ('D', 'tail', 6, 'A'),
        ('E', 'coat', 7, 'F'),
        ('E', 'sit', 8, 'E'),
        ('F', 'sit', 9, 'G'),
    ]
    sm = main()
    action_methods = {
        'sit': sm.sit,
        'coat': sm.coat,
        'tail': sm.tail
    }
    for start_state, action in test_exceptions:
        sm.state = start_state
        try:
            action_methods[action]()
        except MealyError:
            pass
    for s_state, action, e_return, e_state in test_result:
        sm.state = s_state
        result = action_methods[action]()
        assert result == e_return
        assert sm.state == e_state


def main():
    return Mealy()


test()
