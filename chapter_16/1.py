class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

def mul_time(t, x):
    # Переводим всё в секунды
    total_seconds = t.hour * 3600 + t.minute * 60 + t.second
    # Умножаем на x
    total_seconds = total_seconds * x
    # Нормализуем: оставляем в пределах 24 часов
    total_seconds = total_seconds % (24 * 3600)
    
    # Преобразуем обратно в часы, минуты, секунды
    hours = total_seconds // 3600
    total_seconds = total_seconds % 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    
    return Time(int(hours), int(minutes), int(seconds))

def average_speed(race_time, distance):
    # Переводим время гонки в секунды
    total_seconds = race_time.hour * 3600 + race_time.minute * 60 + race_time.second
    # Вычисляем время на единицу расстояния (в секундах)
    seconds_per_unit = total_seconds / distance
    
    # Преобразуем в часы, минуты, секунды
    hours = int(seconds_per_unit // 3600)
    seconds_per_unit = seconds_per_unit % 3600
    minutes = int(seconds_per_unit // 60)
    seconds = seconds_per_unit % 60
    
    return Time(hours, minutes, seconds)

# Пример использования
time = Time(11, 59, 30)
result = mul_time(time, 2)
print(f"Умноженное время: {result.hour}:{result.minute}:{result.second}")

race_time = Time(3, 30, 0)
distance = 42.195
avg = average_speed(race_time, distance)
print(f"Среднее время на км: {avg.hour}:{avg.minute}:{avg.second:.0f}")