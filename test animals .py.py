name = input ('Введите ключку питомца:  ')
vid = input ('Введите вид питомца:  ')
age = int(input ('Введите возраст питомца:  '))
def get_age_form(age: int) -> str:
    if age % 10 == 1 and age % 100 != 11:
        return ("год")
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return ("года")
    else:
        return ("лет")
print (f'Это {vid}, по кличке {name}, Возраст {age} {get_age_form(age)} .')


