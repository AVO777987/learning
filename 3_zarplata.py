try:
    with open('my_file.txt', 'r', encoding='UTF-8') as file:
        content = file.readlines()
    personal = {}
    for string in content:
        personal.update({string.split()[0]: float(string.split()[1])})
    summ = 0
    for key, item in personal.items():
        if item < 20000:
            print(f'У сотрудника {key} зарплата {item} она меньше 20000 рублей')
        summ += item
    salary = summ/len(personal)
    print(f'Средняя зарплата сотрудников равна {round(salary, 2)}')
except IOError:
    print('Файла не существует!!!')

