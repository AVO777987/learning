with open('my_file.txt', 'w', encoding='UTF-8') as file:
    while True:
        message = input('Введите строку для записи в файл')
        if not message:
            break
        file.write(f'{message}\n')

