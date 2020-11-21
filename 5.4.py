my_t = open ("text4.txt","r")
content = my_t.readlines()
from translate import Translator
my_t2 = open ("text4.1.txt", "a")
for i in content:
    translator = Translator(to_lang="Russian")
    translation = translator.translate(i)
    my_t2.write(translation)
    my_t2.write("\n")
my_t2.close()
my_t.close()