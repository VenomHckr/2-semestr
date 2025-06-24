while True:
    s1 = input("Введите текст без пробелов на проверку является ли он палиндромом ")
    s = (s1.lower())
    if s.isalpha():
        print ("принято ", s)
        break 
    else:
        print ("можно вводить только буквы без пробелов и цифр")
        
if s == s[::-1]:
            print("yes")
else:
            print("no")
   