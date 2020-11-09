n = str(input("Введите предложение из нескольких слов:"))
n = n.title()
my_list = n.split ( )
b=0
while b < len(my_list):
    print (b+1, my_list[b][0:10])
    b=b+1