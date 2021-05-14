while(True):
    try:
        value = int(input('Введите колличество секунд для перевода в часы и минуты'))
    except:
        print('Вы ввели не число. Попробуйте еще раз')
        continue
    break
hour = value // 3600
value %= 3600
minutes = value // 60
seconds = value % 60
print(f'{hour}:{minutes}:{seconds}')

