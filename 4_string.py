# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

string = input("Введите строку из нескольких строк").split()

for n in range(len(string)):
    if len(string[n]) > 10:
        print(f'{n+1}.{string[n][:10]}')
    else:
        print(f'{n+1}.{string[n]}')

