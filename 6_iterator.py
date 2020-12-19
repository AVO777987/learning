from itertools import count


def iter_count(number):
    for n in count(number):
        if n == 101:
            break
        print(n)


while True:
    try:
        number = int(input("Введите начальное значение для генерации"))
        break
    except:
        print("Вы ввели не число")
        continue

iter_count(number)