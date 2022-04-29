class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if self.count - other.count > 0:
            return self.count - other.count
        else:
            raise ValueError('The first value is less than the second value')

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, row):
        result = ('*\n' if i % row == 0 else '*' for i in range(1, self.count + 1))
        return ''.join(result)


cell_1 = Cell(20)
cell_2 = Cell(20)

print(cell_1.make_order(3))
