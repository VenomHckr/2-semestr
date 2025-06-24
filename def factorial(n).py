def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    result = [x]
    for k in range(n, 1, -1):
        x = x // k
        result.append(x)
    return result
while True:
    try:
        num = int(input("Введите натуральное число (n ≥ 1): "))
        if num < 1:
            raise ValueError
        break
    except ValueError:
        print("Ошибка! Введите целое число больше 0.")
result = factorial(num)
print(f"Факториалы от {num}! до 1!: {result}")