import random
import bisect  # модуль для бинарного поиска

def random_word_efficient(hist):
    """
    Выбирает случайное слово из гистограммы с учетом частотности
    Использует метод накопленных сумм и бинарный поиск
    """
    # Шаг 1: Получаем списки слов и частот
    words = list(hist.keys())
    freqs = list(hist.values())
    
    # Шаг 2: Строим список накопленных сумм
    cumulative = []
    total = 0
    for freq in freqs:
        total += freq
        cumulative.append(total)
    
    # Шаг 3: Выбираем случайное число от 1 до общего количества слов
    rand_val = random.randint(1, cumulative[-1]) # cumulative[-1] берем последний элемент
    
    # Шаг 4: Находим индекс с помощью бинарного поиска
    # bisect_left возвращает позицию, куда вставить rand_val
    index = bisect.bisect_left(cumulative, rand_val)
    
    # Шаг 5: Возвращаем слово по найденному индексу
    return words[index]