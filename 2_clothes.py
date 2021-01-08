from abc import ABC, abstractmethod


class Clothesabstract(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def expense(self):
        pass


class Clothes(Clothesabstract):
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def expense(self):
        if self.name == 'coat':
            expense = (self.rate / 6.5) + 1
        if self.name == 'suit':
            expense = (self.rate * 2) + 0.3
        return expense


clothes_1 = Clothes('coat', 52)
clothes_2 = Clothes('suit', 10)
print(clothes_1.expense())
print(clothes_2.expense())



