class Complex_Number:
    def __init__(self, com_num_1, com_num_2):
        self.number = complex(com_num_1, com_num_2)

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


com_num_1 = Complex_Number(2, 8)
com_num_2 = Complex_Number(3, 8)
com_num_3 = complex(2, 8)
com_num_4 = complex(3, 8)
print(com_num_1 + com_num_2)
print(com_num_3 + com_num_4)
print(com_num_1 * com_num_2)
print(com_num_3 * com_num_4)