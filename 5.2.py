my_t = open ("text2.txt","r")
content = my_t.readlines()
print (len(content), "строки")
for i in content:
...     print(content.index(i)+1, "строка:", len(i.split()), "слова")
my_t.close()