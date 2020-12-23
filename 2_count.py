try:
    with open('count.txt', 'r', encoding='UTF-8') as file:
        content = file.readlines()
except IOError:
    print('Файла не существует!!!')
print(f'В файле {len(content)} строк ')
n = 1
for string in content:
    print(f'{n} строка - {len(string.split())} слова')
    n += 1
