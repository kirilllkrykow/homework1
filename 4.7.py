def fact(num):
    n = 1
    if num == 0:
        yield f"{num}!=1"
    for el in range(1, num+1):
        n *=el
        yield f"{el}!={n}"
for el in fact(int(input("введите число:"))):
    print(el)            