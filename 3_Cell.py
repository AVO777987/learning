class Cell:
    def __init__(self, count=int):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if other.count >= self.count:
            print('Разница между клетками меньше или равно 0')
        else:
            return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def __str__(self):
        return str(self.count)

    def make_order(self, row):
        result = ''
        for i in range(self.count):
            if (i + 1) % row == 0:
                result = f'{result}*\n'
            else:
                result = f'{result}*'
        return result


cell_1 = Cell(28)
cell_2 = Cell(15)

print(cell_1+cell_2)
print(cell_1-cell_2)
print(cell_1*cell_2)
print(cell_1/cell_2)

print(cell_1.make_order(5))