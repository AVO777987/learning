import datetime


class Data:
    def __init__(self, date_now):
         self.date = date_now

    @classmethod
    def date_to_int(cls, date_now):
        int_date = int(''.join(date_now.split('-')))
        return int_date

    @staticmethod
    def validation_date(date):
        split_date = date.split('-')
        if int(split_date[0]) > 31 or int(split_date[0]) < 1:
              return print('Число может быть от 1 до 31')
        if int(split_date[1]) > 31 or int(split_date[1]) < 1:
              return print('Месяц может быть от 1 до 12')
        return print('Дата введена верно')



date_now = datetime.datetime.now()
date_now = f'{date_now.day}-{date_now.month}-{date_now.year}'
obj_1 = Data(date_now)
print(obj_1.date_to_int(date_now))
obj_1.validation_date('31-12-2021')

