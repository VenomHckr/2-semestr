m = int(input("Введите грузоподьемность лодки "))
if not 1 <= m <= 10e6:
    print ("грузоподъемность должна быть меньше 10 000 000")
    exit() 
n = int(input("Введите коллическво путешественников "))
if not 1 <= n <= 100:
    print ("Колличество путешественников болжно быть не более 100")
    exit()
Ai = [int(input("Введите вес путешественника ")) for _ in range(n)]
if not all(1 <= x <= m for x in Ai):
    print(f"Вес путешественника должен быть от 1 до {m}")
    exit() 
Ai.sort()
left = 0
right = n - 1
boats = 0
while left <= right:
    if Ai[left] + Ai[right] <= m:
        left += 1
    right -= 1
    boats += 1
print("Коллечетво лодок для перепоавки ", boats)