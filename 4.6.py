"""Первый скрипт"""
from itertools import count
from sys import argv
name, n1 = argv
for el in count(int(n1)):
    if el > 15:
        break
    else:
        print (el)
"""Второй скрипт"""
from itertools import cycle
from random import randint
my_list = [randint (0,10) for i in range (5)]
c=int(n1)
for el in cycle (my_list):
    if c>15:
        break
    print (el)
    c+=1