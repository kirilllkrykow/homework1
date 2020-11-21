def my_f():
    x = list(input("Введите список чисел, через пробел:").split())
    while x[-1] != "q":
        n = 0
        sum = int(x[n])
        while n < (len(x) - 1):
            sum = sum + int(x[n + 1])
            n = n + 1
        print (sum)
        f = list(input("Введите еще числа, через пробел:").split())
        x.extend(f)
    else:
        n = 0
        sum = int(x[n])
        while n < (len(x) - 2):
            sum = sum + int(x[n + 1])
            n = n + 1
        print ("Итоговая сумма:")
        return sum
print (my_f())