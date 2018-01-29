class PrintableBoard():

    EMPTY_PLACE = " "

    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.map = []

    def __build(self):
        self.map = []
        for l in range(self.length):
            line = []
            self.map.append(line)
            for w in range(self.width):
                line.append(self.EMPTY_PLACE)

    def add(self, cood, char):
        self.map[cood.y][cood.x] = char

    def clean(self):
        self.__build()

    def __repr__(self):
        to_print = "-" * (self.width + 2) + "\n"
        for line in self.map:
            to_print += '|' + ''.join(line) + "|\n"
        to_print += "-" * (self.width + 2) + "\n"
        return to_print
