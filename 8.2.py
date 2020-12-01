class OwnError(Exception):
    def __init__(self,txt):
        self.txt = txt

def calc():
    try:
        print ("Калькулятор запущен (только деление)")
        a = float(input("Введите делимое:"))
        b = float(input("Введите делитель:"))
        if b == 0:
            raise OwnError("Делить на ноль нельзя!")
    except ValueError:
        return ("Ошибка ввода данных!")
    except OwnError as err:
        return(err)
    else:
        return f"{a/b}:.2f"
print(calc())
