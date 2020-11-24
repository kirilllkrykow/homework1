class Road:
    lenght = 10000
    width = 10

    def __init__(self):
        self._lenght = 10000
        self._width = 10
        print("Длина:", Road.lenght, "м", "Ширина:",Road.width, "м")

    def method (self):
        self.weight = int(input("Введите массу асфальта на 1 квадратный метр толщиной в 1 см:"))
        self.thickness = int(input("Введите трубемую толщину:"))
        print (f"{(self.lenght*self.width*self.weight*self.thickness)/1000:.2f}","тонн")

a = Road()
a.method()