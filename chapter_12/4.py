def load_words(filename):
    """Загружает слова из файла и возвращает множество слов"""
    words = set()
    with open(filename, 'r') as f:
        for line in f:
            word = line.strip().lower()  # убираем пробелы и переводим в нижний регистр
            if word:  # если слово не пустое
                words.add(word)
    # Добавляем однобуквенные слова, которых может не быть в файле
    words.add('a')
    words.add('i')
    return words

def get_children(word):
    """Возвращает список всех слов, получаемых удалением одной буквы"""
    children = []
    for i in range(len(word)):
        # Удаляем букву на позиции i
        child = word[:i] + word[i+1:]
        children.append(child)
    return children

def is_reducible(word, word_set, memo):
    """
    Проверяет, можно ли редуцировать слово до одной буквы
    word: проверяемое слово
    word_set: множество всех допустимых слов
    memo: словарь для кэширования результатов
    """
    # Базовые случаи
    if word in ('a', 'i'):
        return True
    if len(word) == 1:  # другие однобуквенные слова не подходят
        return False
    
    # Проверяем кэш
    if word in memo:
        return memo[word]
    
    # Получаем все потомки
    for child in get_children(word):
        # Проверяем, есть ли потомок в словаре
        if child in word_set:
            # Рекурсивно проверяем потомка
            if is_reducible(child, word_set, memo):
                memo[word] = True
                return True
    
    # Если ни один потомок не подошел
    memo[word] = False
    return False

def find_longest_reducible(words_set):
    """Находит самое длинное редуцируемое слово"""
    # Получаем список всех слов и сортируем по убыванию длины
    words_list = list(words_set)
    words_list.sort(key=len, reverse=True)
    
    memo = {}  # словарь для кэширования
    
    for word in words_list:
        # Пропускаем слишком короткие слова (меньше 3 букв)
        if len(word) < 3:
            continue
        
        print(f"Проверяем слово длиной {len(word)}: {word}")
        if is_reducible(word, words_set, memo):
            return word, len(word)
    
    return None, 0

# Основная программа
if __name__ == "__main__":
    # Загружаем слова
    print("Загружаем словарь...")
    words = load_words('words.txt')  # укажите путь к вашему файлу
    print(f"Загружено {len(words)} слов")
    
    # Ищем самое длинное слово
    print("Ищем самое длинное редуцируемое слово...")
    longest_word, length = find_longest_reducible(words)
    
    if longest_word:
        print(f"\nСамое длинное слово: '{longest_word}'")
        print(f"Длина: {length} букв")
        
        # Для интереса покажем цепочку редукции
        print("\nЦепочка редукции:")
        word = longest_word
        memo_chain = {}
        while len(word) > 1:
            print(word, end=" → ")
            for child in get_children(word):
                if child in words and is_reducible(child, words, memo_chain):
                    word = child
                    break
        print(word)
    else:
        print("Таких слов не найдено")