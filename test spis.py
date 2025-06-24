n = int(input("введите число элементов "))
if not 1<=n<=100000:
    print("введите число менее 100 000 ")
    exit() 
x = list(map(int, input("Введите числа в массив ").split()))
for _ in x:
    if not 1<=_<=100000:
        print("введите число менее 100 000 000 0000")
        exit()
y = [x[-1]] + x[:-1] 
print (y)