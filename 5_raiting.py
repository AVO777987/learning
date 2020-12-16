my_list = [7, 5, 3, 3, 2]
while True:
    try:
        my_number = int(input('Введите число для рейтинга'))
        my_list.append(my_number)
        print(f'Результат: {sorted(my_list, reverse=True)}')
        continue
    except:
        print("Вы ввели не правильное число. Попробуйте еще раз ")
        continue
