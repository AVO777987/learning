def fact(n):
    factorial = 1
    for el in range(1, n + 1):
        factorial *= el
        yield factorial

n = 4

for el in fact(n):
    print(el)

