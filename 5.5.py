my_t = open ("text5.txt", "a")
my_t.write("4 924 290 293 920 84")
my_t.close()
my_t = open ("text5.txt", "r")
content = my_t.readlines()
from functools import reduce
def my_f(el, next_el):
    return el+next_el
n=reduce(my_f,content).split()
g = []
for i in n:
    g.append (float(i))
print(reduce(my_f, g))
my_t.close()