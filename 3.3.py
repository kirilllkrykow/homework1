def my_func():
...     n=int(input("Введите первое число:"))
...     m=int(input("Введите второе число:"))
...     l=int(input("Введите третье число:"))
...     my_list = [n,m,l]
...     my_list.sort()
...     result = f"{my_list[-1]+my_list[-2]}"
...     return result
... print (my_func())