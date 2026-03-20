import datetime

def today():
    x = datetime.date.today()
    day = x.weekday()
    print(f'--> Текущая дата: {x}. День недели:{day}')


today()



from datetime import datetime, timedelta

birthday_str = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
birthday = datetime.strptime(birthday_str, "%d.%m.%Y")

now = datetime.now()  # текущая дата и время

# Возраст
age = now.year - birthday.year
if now.month < birthday.month or (now.month == birthday.month and now.day < birthday.day):
    age -= 1

# Следующий день рождения
next_birthday = birthday.replace(year=now.year)
if next_birthday < now:
    next_birthday = next_birthday.replace(year=now.year + 1)

# Разница
time_left = next_birthday - now

# Вывод
print(f"Возраст: {age}")
print(f"До дня рождения: {time_left}")