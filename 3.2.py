def my_f(**kwargs):
...     return kwargs
... print(my_f(name = str(input("Введите ваше имя:")),\
... surname = str(input("Введите вашу фамилию:")),\
... year = int(input("Введите год рождения:")),\
... city = str(input("Введите город проживания:")),\
... email = str(input("Введите email:")),\
... number = str(input("Введите номер телефона:"))))