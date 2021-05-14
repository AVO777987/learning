while(True):
    try:
        n = int(input('Введите число n которое просуммируем по формуле n + nn + nnn '))
    except:
        print('Вы ввели не число. Попробуйте еще раз')
        continue
    break

summ = n + n**2 + n**3

print(f'n + nn + nnn = {summ}')