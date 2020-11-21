with open("text6.txt") as fobj:
    for line in fobj:
        name, stats = line.split(":")
        name_sum = sum(map(int, "".join([i for i in stats if i== " " or "9" >= i >= "0"]).split()))
        mydict[name] = name_sum
print (f"{mydict}")