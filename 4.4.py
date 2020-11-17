from random import randint
my_list = [randint (0,10) for i in range (5)]
list3 = [num for num in my_list if my_list.count(num)==1]