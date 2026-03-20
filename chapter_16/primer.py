class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

time = Time(11, 59, 30)

def print_time(x):
    print(f'--> Текущее время: {x.hour}:{x.minute}:{x.second}')


def is_after(t1, t2):
    # Сравниваем часы
    if t1.hour > t2.hour:
        return True
    elif t1.hour < t2.hour:
        return False
    # Если часы равны, сравниваем минуты
    elif t1.minute > t2.minute:
        return True
    elif t1.minute < t2.minute:
        return False
    # Если часы и минуты равны, сравниваем секунды
    else:
        return t1.second > t2.second

# Создаем два объекта
t1 = Time(11, 59, 30)
t2 = Time(10, 30, 15)

print(is_after(t1, t2))  # True, так как 11:59:30 позже 10:30:15