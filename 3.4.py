"""Первый вариант"""
def my_func():
    try:
        x=int(input("Введите целое положительное число:"))
        y=int(input("Введите целое отрицательное число:"))
    except ValueError:
        return print ("Неверный формат!")
    if x<0:
        return print ("Первое число отрицательное!")
    elif y>0:
        return print ("Второе число положительное!")
    else: result= f"{x**y:.4f}"
    return result
print (my_func())

"""Второй выриант, через цикл"""
def my_func():
...     try:
...         x=int(input("Введите целое положительное число:"))
...         y=int(input("Введите целое отрицательное число:"))
...     except ValueError:
...         return print ("ошибка: неверный формат!")
...     if x<0:
...         return print ("Ошибка: первое число отрицательное!")
...     elif y>0:
...         return print ("Ошибка: второе число положительное!")
...     else:
...         i=1
...         x1=x
...         while i<abs(y):
...             x1=x1*x
...             i=i+1
...         result = f"{1/x1:.4f}"
...     return result
... print (my_func())