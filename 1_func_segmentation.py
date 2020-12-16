def segmentation(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Деление на ноль!")


while True:
        numbers = input("Введите два числа через пробел которые надо поделить").split()
        if len(numbers) != 2:
            print("Вы ввели больше или меньше двух чисел!")
            continue
        else:
            try:
                a, b = map(int, numbers)
                break
            except:
                print("Вы ввели не число!")
                continue

print(f' Результат {a} / {b} = {segmentation(a, b)}')
