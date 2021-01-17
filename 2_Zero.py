class ZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


while True:
    try:
        dividend = int(input('Введите делимое'))
        division = int(input('Введите делитель'))
        if division == 0:
            raise ZeroDivision('Делитель не может быть нулем!')
        print(dividend / division)
        break
    except ValueError:
        print('Вы ввели не число!!')
        continue
    except ZeroDivision as error:
        print(error)
        continue
