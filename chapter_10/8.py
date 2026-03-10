import random

def check_birthday_paradox(class_size=23, num_trials=10000):
    """
    Оценивает вероятность совпадения дней рождения в группе
    
    Параметры:
    class_size - количество учеников в классе
    num_trials - количество экспериментов
    """
    
    matches = 0  # счетчик экспериментов с совпадениями
    
    for trial in range(num_trials):
        # Генерируем список дней рождения для класса
        # Дни рождения представлены числами от 1 до 365
        birthdays = [random.randint(1, 365) for _ in range(class_size)]
        
        # Проверяем, есть ли совпадения
        # Используем множество: если длина множества меньше длины списка,
        # значит были дубликаты (совпадения дней рождения)
        if len(set(birthdays)) < class_size:
            matches += 1
    
    # Вычисляем вероятность
    probability = matches / num_trials
    
    return probability

# Запускаем эксперимент
num_experiments = 10000
class_size = 23

result = check_birthday_paradox(class_size, num_experiments)

print(f"Количество экспериментов: {num_experiments}")
print(f"Размер класса: {class_size} учеников")
print(f"Количество совпадений: {int(result * num_experiments)}")
print(f"Вероятность совпадения: {result:.2%}")
print(f"Теоретическое значение: ~50.7%")