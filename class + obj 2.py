class Turtle:
    def __init__(self, x=0, y=0, s=1):

        self.x = x
        self.y = y
        self.s = s
    def go_up(self):
        self.y += self.s
        return self
    def go_down(self):
        self.y -= self.s
        return self
    def go_left(self):
        self.x -= self.s
        return self
    def go_right(self):
        self.x += self.s
        return self
    def evolve(self):
        self.s += 1
        return self
    def degrade(self):
        if self.s <= 1:
            raise ValueError("Невозможно уменьшить шаг: размер шага станет ≤ 0")
        self.s -= 1
        return self
    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        steps_x = (dx + self.s - 1) // self.s if self.s > 0 else 0
        steps_y = (dy + self.s - 1) // self.s if self.s > 0 else 0
        return steps_x + steps_y
    def __str__(self):
        return f"Позиция: ({self.x}, {self.y}) "
# Ввод начальных параметров
x = int(input("Введите начальную координату x: "))
y = int(input("Введите начальную координату y: "))
s = int(input("Введите размер шага s: "))

# Создание черепашки с введенными параметрами
t = Turtle(x, y, s)
print("\nНачальное состояние:", t)

# Ввод целевых координат для расчета шагов
x2 = int(input("\nВведите координату перемещения x: "))
y2 = int(input("Введите координату перемещения y: "))

# Выполнение операций и вывод результатов
t.go_right().go_up().go_up()
print("После перемещения:", t)
t.evolve()
try:
    t.degrade()
except ValueError as e:
    print("Ошибка:", e)

# Расчет шагов до введенной цели
print(f"\nМинимальное количество ходов до ({x2}, {y2}): {t.count_moves(x2, y2)}")

# Ввод новых целевых координат
x3 = int(input("\nВведите новую координату перемещения x: "))
y3 = int(input("Введите новую координату перемещения y: "))
print(f"Ходов до ({x3}, {y3}): {t.count_moves(x3, y3)}")