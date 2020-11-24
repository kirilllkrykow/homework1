import time
class TrafficLight:
    color = "Red"

    def __init__(self):
        self.__color = "Red"

    def running(self):
        print(f"{self.color}")
        time.sleep(7)
        self.color = "Yellow"
        print(f"{self.color}")
        time.sleep(2)
        self.color = "Green"
        print(f"{self.color}")
        time.sleep(10)

a = TrafficLight()
a.running()