from abc import ABC, abstractmethod
class Clothes(ABC):
    def sewing(self):
        print("Производится пошив одежды")
class Coat(Clothes):
    def __init__(self):
        self.size = int(input("Введите размер пальто:"))

    @property
    def coat (self):
        print ("Ткани для пошива пальто израсходовано:", f"{self.size/6.5+0.5:.2f}", "метров")

class Suit(Clothes):
    def __init__(self):
        self.height = int(input("Введите рост для костюма:"))

    @property
    def suit (self):
        print ("Ткани для пошива костюма израсходовано:", f"{self.height*2+0.3:.2f}", "метров")

a = Coat()
a.coat
b=Suit()
b.suit
