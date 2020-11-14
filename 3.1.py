def my_f():
...     try:
...         n= int(input("Введите первое число:"))
...         m= int(input("Введите второе число:"))
...     except ZeroDivisionError:
...         print ("Делить на ноль нельзя!")
...     result = f"{(n/m):.2f}"
...     return result
... print (my_f())