class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        print(f'Масса дорожного полотна {self._length*self._width*25*5} тонн')


doroga = Road(10, 10)
doroga.weight()
