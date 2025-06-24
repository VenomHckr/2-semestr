while True:
    try:
        n = int(input("Введите число от 1 до 2 000 000 000: "))
        if 1 <= n <= 2_000_000_000:
            break
        else:
            print("Число должно быть от 1 до 2 000 000 000.")
    except ValueError:
        print("Ошибка: введите целое число.")
divisors = []  
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)  
print(f"Количество делителей: {len(divisors)}")
print("Список делителей:", divisors)

