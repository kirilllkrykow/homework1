from sys import argv
wage, n1, n2, n3 = argv
print (wage)
print ("Количество рабочих часов:", n1)
print ("Ставка в час:", n2)
print ("Премия", n3)
print ("Зарплата:", f"{int(n1)*int(n2)+int(n3)}")
