import random


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str_matrix = ''
        for i in self.matrix:
            for j in i:
                str_matrix = f'{str_matrix}{j}  '
            str_matrix = f'{str_matrix}\n'
        return str_matrix

    def __add__(self, other):
        sum_matrix = []
        for i in range(len(self.matrix)):
            sum_lenght = []
            for j in range(len(self.matrix[i])):
                sum_lenght.append(self.matrix[i][j] + other.matrix[i][j])
            sum_matrix.append(sum_lenght)
        return sum_matrix


matrix_1 = [[random.randint(1, 9) for j in range(1, 5)] for i in range(1, 5)]

matrix_2 = [[random.randint(1, 9) for j in range(1, 5)] for i in range(1, 5)]

matrix1 = Matrix(matrix_1)
matrix2 = Matrix(matrix_2)
print(matrix1)
print(matrix2)
sum_matrix = matrix1 + matrix2

matrix3 = Matrix(sum_matrix)
print(matrix3)

