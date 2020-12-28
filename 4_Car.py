class Car:
    def __init__(self, speed, color, name, is_police=bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        if direction == 'left':
            print(f'Машина {self.name} повернула налево')
        else:
            print(f'Машина {self.name} повернула направо')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость')
        else:
            print(f'Скорость автомобиля {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость')
        else:
            print(f'Скорость автомобиля {self.speed}')


class PoliceCar(Car):
    def __init__(self):
        self.is_police = 'True'


class SportCar(Car):
    pass


car_1 = TownCar(80, 'black', 'Mazda', False)
car_2 = WorkCar(40, 'white', 'BMW', False)
car_3 = PoliceCar(80, 'black', 'Ford', False)
car_4 = SportCar(180, 'blue', 'Lamborgini', False)

car_1.turn('left')
car_2.turn('right')
car_1.show_speed()
print(car_3.name)
print(car_3.is_police)