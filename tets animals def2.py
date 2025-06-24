import collections
def get_age_form(age: int) -> str:
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"
pets = {}
pet_id = 0 
def create():
    global pet_id
    if pets:
        last_id = collections.deque(pets, maxlen=1)[0]
        pet_id = last_id
    pet_id += 1
    name = input('\nВведите кличку питомца: ')
    vid = input('Введите вид питомца: ')
    age = int(input('Введите возраст питомца: '))
    owner = input('Введите имя владельца: ')
    pets[pet_id] = {
        'Кличка': name,
        'Вид': vid,
        'Возраст': age,
        'Владелец': owner
    }
    print(f"Добавлен питомец с ID {pet_id}")
def read():
    try:
        id = int(input("\nВведите ID питомца: "))
        pet = pets.get(id)
        if not pet:
            print("Питомец с таким ID не найден")
            return
        print(f'Это {pet["Вид"]} по кличке "{pet["Кличка"]}". '
              f'Возраст: {pet["Возраст"]} {get_age_form(pet["Возраст"])}. '
              f'Владелец: {pet["Владелец"]}')
    except ValueError:
        print("Некорректный ID")
def update():
    try:
        id = int(input("\nВведите ID питомца для обновления: "))
        if id not in pets:
            print("Питомец с таким ID не найден")
            return
        print("Введите новые данные (оставьте пустым чтобы не менять):")
        name = input('Кличка: ') or None
        vid = input('Вид: ') or None
        age = input('Возраст: ') or None
        owner = input('Владелец: ') or None
        if name: pets[id]['Кличка'] = name
        if vid: pets[id]['Вид'] = vid
        if age: pets[id]['Возраст'] = int(age)
        if owner: pets[id]['Владелец'] = owner
        print("Данные обновлены")
    except ValueError:
        print("Некорректные данные")
def delete():
    try:
        id = int(input("\nВведите ID питомца для удаления: "))
        if id in pets:
            del pets[id]
            print("Питомец удалён")
        else:
            print("Питомец с таким ID не найден")
    except ValueError:
        print("Некорректный ID")
command = ''
while command != 'stop':
    print("\nДоступные команды: create, read, update, delete, stop")
    command = input("Введите команду: ").lower()
    if command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'stop':
        print("Работа завершена")
    else:
        print("Неизвестная команда")
print("\nТекущие записи в базе:")
for id, pet in pets.items():
    print(f"ID {id}: {pet['Кличка']} ({pet['Вид']})")