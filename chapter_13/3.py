def print_top_words(word_counts, n=20):
    """Печатает n наиболее частых слов из словаря word_counts"""
    
    # Шаг 1: Создаем список пар (количество, слово)
    pairs = []
    for word in word_counts:
        count = word_counts[word]  # получаем количество по ключу-слову
        pairs.append([count, word])  # добавляем пару [количество, слово]
    
    # Шаг 2: Сортируем список по количеству (от большего к меньшему)
    # Используем сортировку пузырьком для наглядности
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            # Если текущее количество меньше следующего - меняем местами
            if pairs[i][0] < pairs[j][0]:
                # Меняем местами элементы
                temp = pairs[i]
                pairs[i] = pairs[j]
                pairs[j] = temp
    
    # Шаг 3: Берем первые n элементов
    top_n = pairs[:n]
    
    # Шаг 4: Печатаем результат
    print(f"Топ-{n} самых частых слов:")
    print("-" * 30)
    for i in range(len(top_n)):
        count = top_n[i][0]    # количество
        word = top_n[i][1]      # слово
        print(f"{i+1}. '{word}' — {count} раз")

# Пример использования:
# word_counts = {"hello": 5, "world": 10, "python": 3, "code": 7}
# print_top_words(word_counts, 3)
# Выведет:
# Топ-3 самых частых слов:
# ------------------------------
# 1. 'world' — 10 раз
# 2. 'code' — 7 раз
# 3. 'hello' — 5 раз