from random import randint
my_list = [randint (0,100) for i in range (25)]
list2 = [num for num in my_list if my_list[my_list.index(num)+1]<my_list[my_list.index(num)]]
print (list2)