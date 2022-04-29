from abc import ABC, abstractmethod


class Garment(ABC):
    sum_cons = 0

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def fabric_cons(self):
        pass


class Topcoat(Garment):
    @property
    def fabric_cons(self):
        Garment.sum_cons += self.value / 6.5 + 0.5
        return self.value / 6.5 + 0.5


class Suit(Garment):
    @property
    def fabric_cons(self):
        Garment.sum_cons += 2 * self.value + 0.3
        return 2 * self.value + 0.3


my_coat = Topcoat(10)
my_suit = Suit(5)
any_suit = Suit(3)

print(my_coat.fabric_cons)
print(my_suit.fabric_cons)
print(any_suit.fabric_cons)
print(f'Общий расход ткани: {Garment.sum_cons:.3f}')
