from gameutils.patterns import MetaSingleton
from gameutils.space.directions import Direction


class Cood(metaclass=MetaSingleton):

    def __init__(self, x, y):
        self.id = (x << 32) + y #This hash function will not collide if y.bit_length() <= 32
        self.x = x
        self.y = y

    def to_direction(self, direction, multiplier=1):
        delta = DIRECTION_MAP[direction] * multiplier
        return self + delta

    def __add__(self, other):
        if isinstance(other, Cood):
            return Cood(self.x + other.x, self.y + other.y)
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            return Cood(self.x * other, self.y * other)
        else:
            return self

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

    __rmul__ = __mul__


DIRECTION_MAP = {
    Direction.NORTH: Cood(0, 1),
    Direction.EAST: Cood(1, 0),
    Direction.SOUTH: Cood(0, -1),
    Direction.WEST: Cood(-1, 0),
    Direction.NORTHEAST: Cood(1, 1),
    Direction.SOUTHEAST: Cood(1, -1),
    Direction.SOUTHWEAST: Cood(-1, -1),
    Direction.NORTHWEST: Cood(1, -1)
}
