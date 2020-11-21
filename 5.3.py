my_t = open ("text3.txt","r")
content = my_t.readlines()
from functools import reduce
def my_f(el, next_el):
    return el+next_el
n=reduce(my_f,content).split()
for i in n:
    if n.index(i)%2==0:
        if float(n[n.index(i)+1])<20000:
            print(i)
g=[]
for i in n:
    if n.index(i)%2==1:
         g.append(float(i))
print("Средняя зарплата:", f"{(reduce(my_f,g))/len(g):.2f}")
my_t.close()