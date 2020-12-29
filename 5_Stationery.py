class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")


station_1 = Stationery('Вся канцелярия')
station_2 = Pen('ручкой')
station_3 = Pencil('карандашом')
station_4 = Handle('маркером')

station_1.draw()
station_2.draw()
station_3.draw()
station_4.draw()

