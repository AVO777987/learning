def func_summ(*args):
    summ = 0
    for n in range(len(args[0])):
        summ = summ + (args[0][n])
    return summ

numbers = []
result = 0
count = 0
while True:
    if count == 'q':
        break
    numbers = []
    numbers_list = list(input("Введите числа через пробел которые надо суммировать если введете q то программа закроется ").split())
    for n in range(len(numbers_list)):
        count = numbers_list[n]
        if count == 'q':
            break
        try:
            numbers.insert(n, int(count))
        except:
            print("Вы ввели какой-то другой символ!")
            continue
    result = result + func_summ(numbers)
    print(f'Сумма чисел равна: {result}')
    continue