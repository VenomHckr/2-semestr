a = int(input("Введите колличесво переменных ", ))
count = 0
for _ in range (a):
    n = int(input("Введите переменную ",))
    if n == 0:
        count += 1
print ("Колличество переменых равных нулю", count)