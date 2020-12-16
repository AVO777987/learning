sklad = []
while True:
    id = len(sklad) + 1
    name = input(f'Введите название товара №{id}')
    while True:
        try:
            price = float(input('Введите цену товара'))
            break
        except:
            print('Вы ввели не правильное число. Попробуйте еще раз ')
            continue
    while True:
        try:
            count = int(input('Введите кол-во товара'))
            break
        except:
            print('Вы ввели не правильное число. Попробуйте еще раз ')
            continue
    unit = input('Введите единицу измерения')
    sklad.append((id, {'Название': name, 'цена': price, 'количество': count, 'eд': unit}))
    print(sklad)
    riddle = input("Если хотите добавить еще товар то введите любой символ. Нажмите ENTER если хотите выйти")
    if riddle == '':
        break
analitic = {}
for n in sklad:
    for key, value in n[1].items():
        if key in analitic:
            if value in analitic[key]:
                continue
            analitic[key].append(value)
        else:
            analitic[key] = [value]
print(analitic)

