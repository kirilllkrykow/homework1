class Worker:
    name = "Иван"
    surname = "Иванов"
    position = "Врач"
    income = "150000"

    def __init__(self):
        self._income = {"wage": int(input("Введите оклад:")), "bonus": int(input("Введите премию:"))}

class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income.get("wage")+self._income.get("bonus"))

a=Position()
a.get_full_name()
a.get_total_income()