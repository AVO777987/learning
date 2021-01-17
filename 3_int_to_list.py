class Validation_value(Exception):
    def __init__(self, text):
        self.text = text


int_list = []
while True:
    try:
        value = input('Введите число, если хотите выйти введите stop')
        if value == 'stop':
            break
        if not value.isdigit():
            raise Validation_value('Вы ввели не число!!!')
        int_list.append(int(value))
    except Validation_value as error:
        print(error)
        continue

print(int_list)
