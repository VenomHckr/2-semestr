n = int(input("Введите количество элементов 1 списка  "))
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
            else: 
                x.add(m)
                break
        except ValueError:
            print("Ошибка: введите целое число")
m = int(input("Введите колличество элементов 2 списка  "))
while not (1<= m <= 100000):
    print("введите n от 1 до 100 000")
    m = int(input("повторите ввод  "))
y = set()
for _ in range(m):
    while True:
        try:
            m = int(input())
            if m in y:
                print("Такой элемент присутствует в множестве")
                continue
            else: 
                y.add(m)
                break
        except ValueError:
            print("Ошибка: введите целое число")
print("колличество элементов 1 списка", len(y))
print("колличество элементов 2 списка", len(x))
print(x)
print(y)
