class Date:
    def __init__(cls,date):
          pass

    @classmethod
    def time(cls,date):
        date = date.split("-")
        print (int(date[0]),int(date[1]),int(date[2]))

    @staticmethod
    def test(date):
        date = date.split("-")
        if int(date[0])<0:
            print ("Ошибка ввода дня")
        if int(date[0])>31:
            print("Ошибка ввода дня")
        if int(date[1])<0:
            print("Ошибка ввода месяца")
        if int(date[1])>12:
            print("Ошибка ввода месяца")
        if int(date[2])>2020:
            print("Ошибка ввода года")
        else:
            print ("Данные введены верно")
Date.test("20-03-2019")
Date.time("19-03-2018")
Date("16-04-2017")