def summ (*args):
    return sorted(list(args[0]), reverse=True)[0] + sorted(list(args[0]), reverse=True)[1]


while True:
    try:
        numbers = list(map(int, input("Введите числа через пробел которые надо сложить").split()))
        print(summ(numbers))
        break
    except:
        print("Вы ввели не числа")
        continue
