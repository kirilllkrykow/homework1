def my_f():
...     try:
...         my_t = open("text.txt", "a")
...         i = my_t.write(str(input("Введите что-нибудь:")))
...         my_t.write("\n")
...         while i != 0:
...             i = my_t.write(str(input("Введите ещё что-нибудь:")))
...             my_t.write("\n")
...         else:
...             my_t.close()
...             my_t = open("text.txt", "r")
...             for line in my_t:
...                 print(line)
                my_t.close()
...     except IOError:
...         print("Произошла ошибка ввода-вывода!")
... print (my_f())