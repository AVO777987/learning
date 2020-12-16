string = input("Введите строку из нескольких строк").split()

for n in range(len(string)):
    if len(string[n]) > 10:
        print(f'{n+1}.{string[n][:10]}')
    else:
        print(f'{n+1}.{string[n]}')

