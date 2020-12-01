class Storage:
    volume = 500
    equip = "equip"

    def __init__(self):
        pass

    @classmethod
    def input(cls):
        global equip
        equip = {"print": 200, "scan": 100, "copy": 75, "other": 25, "empty": 100}
        print("Доброе утро! Сегодня есть новые поставки техники на склад!")
        try:
            a = int(input("Сколько принтеров привезли?"))
            b = int(input("Сколько сканеров привезли?"))
            c = int(input("Сколько ксероксов привезли?"))
            if a + b + c > equip.get("empty"):
                print("На складе недостаточно места!", a + b + c - equip.get("empty"),
                      "единиц техники придется отправить обратно.")
                print("Свободного метста на складе:", equip.get("empty"))
                a = int(input("Сколько принтеров принять на склад?"))
                print("Свободного метста на складе:", equip.get("empty") - a)
                b = int(input("Сколько сканеров принять на склад?"))
                print("Свободного метста на складе:", equip.get("empty") - a - b)
                c = int(input("Сколько ксероксов принять на склад?"))
                equip.update(
                    {"print": equip.get("print") + a, "scan": equip.get("scan") + b, "copy": equip.get("copy") + c,
                     "empty": equip.get("empty") - a - b - c})
            else:
                equip.update(
                    {"print": equip.get("print") + a, "scan": equip.get("scan") + b, "copy": equip.get("copy") + c,
                     "empty": equip.get("empty") - a - b - c})
        except ValueError:
            print("Введено не числовое значение")
        else:
            print("Загрузка завершена! На складе сейчас:", equip.get("print"), "принтеров", equip.get("scan"),
                  "сканеров и", equip.get("copy"), "ксероксов.", "Cвободного места:", equip.get("empty"))

    @classmethod
    def output(cls):
        print("Начинаем отгрузку, всего доступно:", equip.get("print"), "Принтеров", equip.get("scan"), "Сканеров и",
              equip.get("copy"), "ксероксов")
        z = "нет"
        while z[1] != "а":
            try:
                n = int(input("Введите номер подразделения для отгрузки оргтехники"))
                print("Отгрузка в подразделение №", n)
                a = int(input("Сколько отгрузить принтеров?"))
                b = int(input("Сколько отгрузить сканеров?"))
                c = int(input("Сколько отгрузить ксероксов?"))
                print("Отгрузка в подразделение №", n, "завершена")
                equip.update(
                    {"print": equip.get("print") - a, "scan": equip.get("scan") - b, "copy": equip.get("copy") - c,
                     "empty": equip.get("empty") + a + b + c})
                print("На складе осталось:", equip.get("print"), "принтеров", equip.get("scan"), "сканеров и",
                      equip.get("copy"), "ксероксов.", "Свободного места:", equip.get("empty"))
                z = str(input("Отгрузка завершена?"))
            except ValueError:
                print("Введено не числовое значение")
        else:
            print("Отгрузка завершена")

    @classmethod
    def show(cls):
        print("На складе осталось:", equip.get("print"), "принтеров", equip.get("scan"), "сканеров и",
              equip.get("copy"), "ксероксов.", "Свободного места:", equip.get("empty"))

class Equip:
    type = "type"
    value = "value"
    number = "number"

class Printer(Equip):
    type = "type"
    speed_of_print = "30"

class Scan(Equip):
    brand = "Xerox"
    speed = "8"

class Copier(Equip):
    brand = "hp"
    size = "800"

Storage.input()
Storage.output()
Storage.show()
