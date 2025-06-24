class CashRegister:
    def __init__(self, initial_amount=0.0):
        if initial_amount < 0:
            raise ValueError("Начальная сумма не может быть отрицательной")
        self.amount = initial_amount
    
    def top_up(self, x):
        if x <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.amount += x
        print(f"Касса пополнена на {x:.2f} руб. Текущий баланс: {self.amount:.2f} руб.")
    
    def take_away(self, x):
        if x <= 0:
            raise ValueError("Сумма изъятия должна быть положительной")
        if x > self.amount:
            raise ValueError(f"Недостаточно денег в кассе. Требуется: {x:.2f} руб., доступно: {self.amount:.2f} руб.")
        self.amount -= x
        print(f"Из кассы изъято {x:.2f} руб. Текущий баланс: {self.amount:.2f} руб.")
    
    def count_1000(self):
        thousands = int(self.amount // 1000)
        print(f"В кассе {thousands} полных тысяч рублей")
        return thousands
    
    def __str__(self):
        return f"Текущий баланс: {self.amount:.2f} руб. | Целых тысяч: {self.count_1000()}"

# касса
try:
    start_amount = float(input("Введите начальную сумму в кассе: "))
    kassa = CashRegister(start_amount)
    print(f"Касса создана с начальной суммой {start_amount:.2f} руб.")
except ValueError as e:
    print(f"Ошибка создания кассы: {e}")
    kassa = CashRegister()
    print("Создана касса с нулевым балансом")

#  меню
while True:
    print("\n" + "="*50)
    print("1: Пополнить кассу")
    print("2: Изъять деньги из кассы")
    print("3: Показать количество полных тысяч")
    print("4: Показать состояние кассы")
    print("5: Выйти")
    
    choice = input("Выберите операцию (1-5): ")
    
    if choice == '1':
        try:
            amount = float(input("Введите сумму для пополнения: "))
            kassa.top_up(amount)
        except ValueError as e:
            print(f"Ошибка: {e}")
    
    elif choice == '2':
        try:
            amount = float(input("Введите сумму для изъятия: "))
            kassa.take_away(amount)
        except ValueError as e:
            print(f"Ошибка: {e}")
    
    elif choice == '3':
        kassa.count_1000()
    
    elif choice == '4':
        print(kassa)
    
    elif choice == '5':
        print("Работа с кассой завершена")
        break
    else:
        print("Некорректный ввод. Пожалуйста, выберите 1-5")