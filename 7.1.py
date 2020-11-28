import numpy as np
from random import randint
class Matrix():
    value = "value"

    def __init__(self):
        self.value = np.array([[randint (-99,99) for i in range (5)],[randint (-99,99) for i in range (5)],[randint (-99,99) for i in range (5)]])

    def __str__(self):
        return str(self.value)

    def __add__(self,other):
        return(self.value+other.value)
a=Matrix()
b=Matrix()
print(a)
print(a+b)