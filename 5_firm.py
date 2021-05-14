while(True):
    try:
        proceeds = int(input('Введите прибыль фирмы'))
        loss = int(input('Введите издержки фирмы'))
    except:
        print('Вы ввели не число. Попробуйте еще раз')
        continue
    break
if proceeds > loss:
    print('Ваша фирма работает в прибыль')
    profit = proceeds - loss
    print(f'Прибыль вашей фирмы {profit}')
    while(True):
        try:
            coworkers = int(input('Введите колличество сотрудников в Вашей фирме'))
        except:
            print('Вы ввели не число. Попробуйте еще раз')
            continue
        break
    print(f'Ваша прибыль на каждого сотрудника являеться {profit/coworkers}')
else:
    print('Ваша фирма работает в убыток')