import time



def today():
    days = time.time() // 86400
    h = (time.time() % 86400) // 3600
    m = (time.time() % 86400) % 3600
    min = m // 60
    s = m % 60
    
    print(f'Текущее время {h} часов, {min} минут, {s} секунд. Прошло {int(days)} дней')

today()





