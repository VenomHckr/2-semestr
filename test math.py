n = float(input("Введите пятизначное число  "))
one = n % 10
ten = (n // 10) % 10
hundred = (n // 100) % 10
thousand = (n //1000) % 10
tenthousand = (n // 10000) % 10
x = ten ** one * hundred // (tenthousand - thousand) 
print("единицы ", one) 
print("десятки ", ten)
print("сотни ", hundred)
print("тысячи ", thousand)
print("десятки тысяч ", tenthousand)
print("Ответ  ", x)