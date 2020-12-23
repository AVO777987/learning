learning = {}
try:
    with open('my_file.txt', 'r', encoding='UTF-8-sig') as file:
        for line in file:
            content = line.split()
            for string in content:
                print(string)
                string.replace(':', '').replace('(л)', '').replace('(пр)', '').replace('(лаб).', '').replace('(лаб)', '')
                print(string)
except IOError:
    print('Файла не существует!!!')