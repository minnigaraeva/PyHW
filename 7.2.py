from abc import ABC, abstractmethod


class Clothes(ABC):
    sum_consumption = 0

    @abstractmethod
    def calc_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.sum_consumption += self.calc_consumption

    def __str__(self):
        return f'Material consumption for this coat is {self.calc_consumption:.2f}'

    @property
    def calc_consumption(self):
        coat_consumption = self.size / 6.5 + 0.5
        return float(f'{coat_consumption:.2f}')


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Suit.sum_consumption += self.calc_consumption

    def __str__(self):
        return f'Material consumption for this suit is {self.calc_consumption:.2f}'

    @property
    def calc_consumption(self):
        suit_consumption = 2 * float(self.height) + 0.3
        return float(f'{suit_consumption:.2f}')


coat = Coat(6)
suit = Suit(7)
coat_2 = Coat(5)
print(coat)
print(coat_2)
print(suit)
print(f'{Coat.sum_consumption:.2f}')
print(f'{Suit.sum_consumption:.2f}')

