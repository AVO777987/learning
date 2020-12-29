import time


class TrafficLight:
    __color = 'зеленый'

    def running(self, curent_color):
        if curent_color == 'красный':
            if self.__color == 'зеленый':
                self.__color = curent_color
                print(self.__color)
            else:
                print('Не правильный порядок цвета')
                exit()
        if curent_color == 'желтый':
            if self.__color == 'красный':
                self.__color = curent_color
                print(self.__color)
            else:
                print('Не правильный порядок цвета')
                exit()
        if curent_color == 'зеленый':
            if self.__color == 'желтый':
                self.__color = curent_color
                print(self.__color)
            else:
                print('Не правильный порядок цвета')
                exit()


trafficlight = TrafficLight()
while True:
    trafficlight.running('красный')
    time.sleep(7)
    trafficlight.running('желтый')
    time.sleep(2)
    trafficlight.running('зеленый')
    time.sleep(7)
    trafficlight.running('зеленый')

