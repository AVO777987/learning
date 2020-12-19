def fact(n):
    factorial = 1
    for el in range(1, n):
        factorial *= el
        yield factorial

n = 10

for el in fact(n):
    print(el)

