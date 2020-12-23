try:
    with open('numbers.txt', 'r', encoding='UTF-8-sig') as file:
        new_list = []
        for line in file:
            line_number = line.split(' — ')
            if line_number[0] == 'One':
                line_number[0] = 'Один'
            if line_number[0] == 'Two':
                line_number[0] = 'Два'
            if line_number[0] == 'Three':
                line_number[0] = 'Три'
            if line_number[0] == 'Four':
                line_number[0] = 'Четыре'
            new_list.append(line_number)
except IOError:
    print('Файла не существует!!!')
with open('new_file.txt', 'w', encoding='UTF-8-sig') as file:
    for line in new_list:
        print(line)
        print(f'{line[0]} — {line[1]}', file=file)
