my_list=list(range(50,501))
from functools import reduce
def my_f(el, el_next):
     return el * el_next
print (reduce(my_f, [num*2 for num in my_list]))