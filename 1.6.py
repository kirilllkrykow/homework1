a = int(input("Введите результат вашей пробежки в первый день:"))
b = int(input("Введите желаемый результат:"))
day=1
while a<b:
...     a=a*1.1
...     day +=1
... print(day, "Congratulations!")