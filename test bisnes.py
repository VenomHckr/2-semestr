x = int(input("Минимальная сумма инвестиций:  "))
a = int(input("Колличество долларову у Mike:  "))
b = int(input("Колличество долларову у Ivan: "))
if a >= x and b < x:
    print ("Mike")
elif b >= x and a < x:
    print ("Ivan")
elif a >= x and b >= x:
    print (2)
elif x <= a + b:
    print (1)
else:
    print(0)