class Car():
    speed = 100
    color = "Синий"
    name = "Lamborgini"
    is_police = False

    def __init__(self):
        self.speed = int(input("Введите скорость:"))
        self.color = str(input("Введите цвет автомобиля:"))
        self.name = str(input("Введите марку автомобиля:"))

    def go(self):
        print("Автомобиль поехал")

    def stop(self):
        print("Автомобиль остановился")

    def turn_right(self):
        print("Автомобиль повернул направо")

    def show_speed(self):
        print(self.speed)

class SportCar(Car):
    def __init__(self):
        self.speed = int(input("Введите скорость:"))
        self.color = str(input("Введите цвет автомобиля:"))
        self.name = str(input("Введите марку автомобиля:"))

class PoliceCar(Car):
    def __init__(self):
        self.is_police = True
        self.speed = int(input("Введите скорость:"))
        self.color = str(input("Введите цвет автомобиля:"))
        self.name = str(input("Введите марку автомобиля:"))

class WorkCar(Car):
    def __init__(self):
        n = str(input("Это полицейская машина?"))
        if n == "да":
            self.is_police = True
        else:
            self.is_police = False
        self.speed = int(input("Введите скорость:"))
        self.color = str(input("Введите цвет автомобиля:"))
        self.name = str(input("Введите марку автомобиля:"))

    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print("Превышение скорости на:", self.speed - 40, "км/ч")

class TownCar(Car):
    def __init__(self):
        n = str(input("Это полицейская машина?"))
        if n == "да":
            self.is_police = True
        else:
            self.is_police = False
        self.speed = int(input("Введите скорость:"))
        self.color = str(input("Введите цвет автомобиля:"))
        self.name = str(input("Введите марку автомобиля:"))

    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print("Превышение скорости на:", self.speed - 60, "км/ч")

a = Car()
a.go()
a.stop()
print(a.color)
b = TownCar()
c = PoliceCar()
b.self_speed()