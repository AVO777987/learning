def fact(n):
    factorial = 1
    for el in range(1, n + 1):
        factorial *= el
        yield factorial


while True:
    try:
        n = int(input('Укажите факториал какого числа Вы хотели бы узнать?'))
        break
    except:
        print("Вы введи не число")
        continue

for el in fact(n):
    print(el)

