
while True:
    try:
        a = int(input("Введите число А " ))
        b = int(input("Введите число В больше либо равное А " ))
        if a <= b:
            break
        else: 
            print("Чиcло A болжно быть меньше или рано В")
    except ValueError:
        print("Ошибка: введите целое число.")      
for a in range (a, b):
    if a % 2 == 0:  
        print (a)        
