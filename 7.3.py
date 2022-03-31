class Cell:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'We have a cell with {self.num} parts'

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num > other.num:
            return Cell(self.num - other.num)
        return f'Second cell is bigger then first'

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, num_line):
        line = ['*' * num_line] * (self.num // num_line)
        line.append('*' * (self.num % num_line))
        return '\n'.join(line)


cell_1 = Cell(12)
cell_2 = Cell(7)
print(cell_1.__add__(cell_2))
print(cell_1.__sub__(cell_2))
print(cell_1.__mul__(cell_2))
print(cell_1.__truediv__(cell_2))
print(cell_1.make_order(4))
print(cell_2.__sub__(cell_1))
print(cell_2.make_order(5))
