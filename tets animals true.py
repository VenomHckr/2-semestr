def get_age_form(age: int) -> str:
    if age % 10 == 1 and age % 100 != 11:
        return ("год")
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return ("года")
    else:
        return ("лет")
pets = {}
n = int(input("Введите колличество питомцев  "))
for i in range(n):
    name =  input ('Введите кличку питомца:  ')
    pet_owner = input ('Введите Ваше имя:  ')
    vid = input ('Введите вид питомца:  ')
    age = int(input ('Введите возраст питомца:  '))
    pets[name] = {
        'Вид питомца': vid,
        'Возраст питомца': age,
        'Имя владельца': pet_owner}
for name in pets.keys():  
    pet_info = pets[name]
    values = list(pet_info.values())
    vid = values[0]
    age = values[1]
    pet_owner = values[2]
    print (f'Это {vid}, по кличке {name}, Возраст {age} {get_age_form(age)}, Имя владельца {pet_owner} .')
    