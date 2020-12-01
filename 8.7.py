class Complex():
    p = "p"

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p = complex(int(self.p1), int(self.p2))

    def __add__(self, other):
        return self.p + other.p

    def __mul__(self, other):
        return self.p * other.p

a=Complex(1,3)
b=Complex(5,2)
a.__add__(b)
a.__mul__(b)