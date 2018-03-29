
class AdditionQuestion:

    def __init__(self, first, second, correct, other):
        self.firstSummand = first
        self.secondSummand = second
        self.correct = correct
        self.others = other

    # override to return a tuples of the values
    def __iter__(self):
        return iter([('firstSummand', self.firstSummand),
                     ('secondSummand', self.secondSummand),
                     ('correct', self.correct),
                     ('other', self.others)])
