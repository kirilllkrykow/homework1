class Cell():
    number2 = "pass"
    def __init__(self,number):
        self.number = number
        print ("Количество ячеек:", self.number)
    def __add__(self,other):
        return (self.number + other.number)

    def __sub__(self,other):
        if self.number-other.number <0:
            return ("0")
        else:
            return (self.number-other.number)

    def __mul__(self,other):
        return (self.number*other.number)

    def __floordiv__(self,other):
        if self.number<other.number:
            return ("0")
        else:
            return (self.number//other.number)

    def make_order(self,number2):
        self.number2 = number2
        n=0
        while n<self.number//int(self.number2):
            print ("*"*int(self.number2),"\n")
            n+=1
        else:
            print ("*"*(int(self.number)%int(number2)))

a = Cell(19)
b = Cell (16)
print (a+b)
print (a-b)
print (a//b)
print (a*b)
a.make_order(5)