from utils.patterns import MetaSingleton

class Cood(metaclass=MetaSingleton):

    def __init__(self, x, y):
        self.id = hash((x, y))
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Cood):
            return self.id == other.id
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.id

    def __repr__(self):
        return "Cood: ({}, {})".format(self.x, self.y)
