class NewError(Exception):
    def __init__(self,txt):
        self.txt = txt

def my_f():
    b = []
    a = input("Введите первое число:")
    while a != "stop":
        try:
            if a.isnumeric() == False:
                raise NewError ("Это не совсем число, попробуйте еще раз")
        except NewError as err:
            print (err)
            a = input("Введите число или stop для окончания:")
        else:
            b.append(a)
            a = input("Введите новое число или stop для окончания:")
    else:
        return b