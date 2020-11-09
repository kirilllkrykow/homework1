my_list = list(input("Введите список значений:"))
n=0
while n<len(my_list):
...     my_list1=my_list[n:n+2]
...     my_list1.reverse()
...     my_list[n:n+2]=my_list1
...     n=n+2
... else: print ("список окончен")