n = int(input("Введите число строк "))
if not 1 <= n <= 10000:
    print ("Введите число менее 10 000")   
    exit ()
x = []
for _ in range(n): 
    n1 = int(input("Введите число в строку менее 10 000 "))
    if abs(n1) > 10000:
        print ("Введите число менее 10 000") 
        exit ()
    x.append(n1)
x1 = x[::-1]
print (x1)        