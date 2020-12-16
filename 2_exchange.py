exchange_list = list(input('Введите значения в список для обмена значений через пробел'))
print(f'Исходный список   : {exchange_list}')
element = 0
for n in range(int(len(exchange_list)/2)):
    exchange_list[element], exchange_list[element + 1] = exchange_list[element + 1], exchange_list[element]
    element += 2
print(f'Изменённый список : {exchange_list}')
