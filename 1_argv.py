from sys import argv


def parse_argv(argv):
    print(argv)
    for n in range(len(argv)):
        if argv[n] == '-time':
            try:
                time = int(argv[n+1])
            except:
                print('Введите время работы в цифрах')
                return
        elif argv[n] == '-rate':
            try:
                rate = int(argv[n+1])
            except:
                print('Введите ставку в час в цифрах')
                return
        elif argv[n] == '-prize':
            try:
                prize = int(argv[n+1])
            except:
                print('Введите премию в цифрах')
                return
    return (time * rate) + prize


print(f' Зарплата сотрудника равна: {parse_argv(argv)}')
