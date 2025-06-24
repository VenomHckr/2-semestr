import re
s1 = input("Введите текст до 1000 символов ")
s2 = len(s1)
if s2 <= 1000:
    s = re.sub(r' +', ' ' , s1)
    print (s)
else: 
    print ("Введите меньшее колличесво символов")
