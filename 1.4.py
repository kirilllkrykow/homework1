n = int(input("Введите любое целое положительное число:"))
Max=0
while n >= 10:
...     b = n % 10
...     if max < b:
...         max=b
...     n = n // 10
... else: print (max)