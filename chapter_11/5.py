def rotate_word(word, shift):
    """Поворачивает слово на указанное количество позиций"""
    if not word:
        return word
    shift = shift % len(word)  # Нормализуем сдвиг
    if shift == 0:
        return word
    return word[shift:] + word[:shift]

def find_rotation_pairs(words):
    """
    Находит все пары ротации в списке слов
    Возвращает словарь, где ключ - слово, значение - список слов-ротаций
    """
    # Преобразуем список в множество для быстрого поиска
    word_set = set(words)
    pairs = {}
    processed = set()  # Множество уже обработанных слов
    
    for word in words:
        if word in processed:
            continue
            
        # Находим все ротации текущего слова
        rotations = []
        for shift in range(1, len(word)):  # Проверяем все возможные сдвиги
            rotated = rotate_word(word, shift)
            if rotated in word_set and rotated != word:
                rotations.append(rotated)
                processed.add(rotated)
        
        # Если нашли ротации, добавляем в результат
        if rotations:
            pairs[word] = rotations
            processed.add(word)
    
    return pairs

# Пример использования
word_list = ["abc", "bca", "cab", "xyz", "yzx", "hello", "elloh", "llohe", "world"]
result = find_rotation_pairs(word_list)

# Выводим результаты
for word, rotations in result.items():
    print(f"{word} -> {', '.join(rotations)}")
