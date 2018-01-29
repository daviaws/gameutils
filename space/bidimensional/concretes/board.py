import random

from gameutils.space.bidimensional.abstractions import Cood


class Board():

    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.board = {}
        self.elements = []
        self.__build(width, length)

    def __build(self, width, length):
        for x in range(width):
            for y in range(length):
                cood = Cood(x, y)
                self.board[cood] = cood
                self.elements.append(cood)

    def unavailable(self, cood):
        del self.board[cood]
        self.elements.remove(cood)

    def available(self, cood):
        self.board[cood] = cood
        self.elements.append(cood)

    def in_bounds(self, cood):
        return cood in self.board

    def random_pick(self):
        return random.choice(self.elements)

    def __repr__(self):
        return str(self.board)
