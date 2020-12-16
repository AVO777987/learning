def exponentiation(*args):
    a = (args[0][0]**args[0][1])
    b = 1
    for n in range(abs(args[0][1])):
        b = b * (1 / args[0][0])
    return a, b


while True:
    try:
        numbers = list(map(int, input("Введите два числа через пробел которые надо возвести в степень ").split()))
        if len(numbers) != 2:
            print("Вы не ввели два числа")
            continue
        numbers[1] = abs(numbers[1]) * -1
        print(exponentiation(numbers))
        break
    except:
        print("Вы ввели не числа")
        continue



