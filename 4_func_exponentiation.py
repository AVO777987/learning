#def exponentiation(x, y):
    # a = 1 / (x**y)
    # for n in abs(y):
    #     result = result * (1 / x)
    # return result

# exponentiation(1,-2)


x = 2
y = -3
a = (x**y)
b = 1
for n in range(abs(y)):
    b = b * (1 / x)
print(a)
print(b)