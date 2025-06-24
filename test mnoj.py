n = int(input())
while not (1<= n <= 100000):
    print("введите n от 1 до 100 000")
    n = int(input("повторите ввод  "))
x = set()
for _ in range(n):
    while True:
        try:
            m = int(input())
            if m in x:
                print("Такой элемент присутствует в множестве")
                continue
            elif abs(m) > 2*10e9:
                print ("Введите число меньше 20 000 000 000")
                continue
            else: 
                x.add(m)
                break
        except ValueError:
            print("Ошибка: введите целое число")
b = sorted(x)
print("колличество элементов", len(x))
print(b)


