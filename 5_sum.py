with open('summ.txt', 'w', encoding='UTF-8-sig') as file:
    numbers = input('Введите числа через пробел')
    print(f'{numbers}', file = file)
try:
    with open('summ.txt', 'r', encoding='UTF-8-sig') as file:
        content = file.read()
        numbers = content.split()
        summ = 0
        for n in numbers:
            try:
                summ += int(n)
            except:
                continue
    print(summ)
except IOError:
    print('Файла не существует!!!')
