class Worker:
    def __init__(self, name, surname, position, income={'wage', "bonus"}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.surname} {self.name}')

    def get_total_income(self):
        income = int(self._income["wage"]) + int(self._income["bonus"])
        print(income)


worker_1 = Position('Андрей', 'Володин', 'Системный администратор', {"wage": 80000, "bonus": 20000})
worker_2 = Position('Иван', 'Пупкин', 'Слесарь', {"wage": 60000, "bonus": 10000})
worker_1.get_full_name()
worker_1.get_total_income()
worker_2.get_full_name()
worker_2.get_total_income()

