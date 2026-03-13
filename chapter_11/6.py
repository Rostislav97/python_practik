import os

# ============================================================
# ЧАСТЬ 1: ЗАГРУЗКА ДАННЫХ (адаптируйте под реальные файлы)
# ============================================================

def read_dictionary_pronounce(filename='c06d'):
    """
    Читает словарь произношений CMU.
    В реальности файл c06d имеет формат:
    WORD  произношение
    Например: "WRACK  W R AE K"
    """
    pron_dict = {}
    try:
        with open(filename, 'r', encoding='latin-1') as f:
            for line in f:
                # Пропускаем комментарии (начинаются с #)
                if line.startswith('#'):
                    continue
                
                # Разделяем слово и произношение
                parts = line.strip().split(' ', 1)
                if len(parts) == 2:
                    word, pron = parts
                    # Приводим слово к верхнему регистру для единообразия
                    pron_dict[word.upper()] = pron.strip()
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Использую тестовые данные.")
        # Тестовые данные для демонстрации работы
        test_data = {
            'WRACK': 'W R AE K',
            'RACK': 'R AE K',
            'WACK': 'W AE K',
            'PLANE': 'P L EY N',
            'PLAN': 'P L AE N',
            'LANE': 'L EY N',
            'SNEAK': 'S N IY K',
            'SNEAK': 'S N IY K',  # дубликат для демонстрации
            'NEAK': 'N IY K',
            'SEAK': 'S IY K',
        }
        pron_dict.update(test_data)
    
    return pron_dict

def read_word_list(filename='words.txt'):
    """
    Читает список английских слов.
    В реальности это может быть файл со словами, по одному на строку.
    """
    word_set = set()
    try:
        with open(filename, 'r') as f:
            for line in f:
                word_set.add(line.strip().lower())
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Использую тестовые данные.")
        # Тестовые слова для демонстрации
        test_words = ['wrack', 'rack', 'wack', 'plane', 'plan', 'lane', 
                     'sneak', 'neak', 'seak', 'brain', 'rain', 'bane', 
                     'train', 'rain', 'tain']
        word_set.update(test_words)
    
    return word_set

# ============================================================
# ЧАСТЬ 2: ОСНОВНАЯ ФУНКЦИЯ ПОИСКА РЕШЕНИЙ
# ============================================================

def find_puzzle_words(word_set, pron_dict):
    """
    Ищет все пятибуквенные слова, удовлетворяющие условиям головоломки.
    
    Аргументы:
        word_set: множество всех допустимых слов
        pron_dict: словарь произношений (слово -> строка произношения)
    
    Возвращает:
        список найденных слов-решений
    """
    solutions = []
    
    # Перебираем все слова в множестве
    for word in word_set:
        # 1. Оставляем только пятибуквенные слова
        if len(word) != 5:
            continue
        
        word_upper = word.upper()
        
        # 2. Проверяем, есть ли произношение у исходного слова
        if word_upper not in pron_dict:
            continue
        
        original_pron = pron_dict[word_upper]
        
        # 3. Получаем слово без первой буквы
        word_no_first = word[1:]  # слово из 4 букв
        word_no_first_upper = word_no_first.upper()
        
        # Проверяем существование слова и его произношения
        if word_no_first not in word_set:
            continue
        if word_no_first_upper not in pron_dict:
            continue
        
        pron_no_first = pron_dict[word_no_first_upper]
        
        # 4. Проверяем первое условие (омофон после удаления 1-й буквы)
        if original_pron != pron_no_first:
            continue
        
        # 5. Получаем слово без второй буквы
        word_no_second = word[0] + word[2:]  # слово из 4 букв
        word_no_second_upper = word_no_second.upper()
        
        # Проверяем, чтобы это было ДРУГОЕ слово (не то же, что без первой буквы)
        if word_no_second == word_no_first:
            continue
            
        # Проверяем существование второго слова
        if word_no_second not in word_set:
            continue
        if word_no_second_upper not in pron_dict:
            continue
        
        pron_no_second = pron_dict[word_no_second_upper]
        
        # 6. Проверяем второе условие (омофон после удаления 2-й буквы)
        if original_pron != pron_no_second:
            continue
        
        # Если дошли до сюда — слово удовлетворяет всем условиям!
        solutions.append(word)
    
    return solutions

# ============================================================
# ЧАСТЬ 3: ЗАПУСК ПРОГРАММЫ И ВЫВОД РЕЗУЛЬТАТОВ
# ============================================================

def main():
    print("Загрузка словарей...")
    
    # Загружаем список слов и словарь произношений
    word_set = read_word_list()
    pron_dict = read_dictionary_pronounce()
    
    print(f"Загружено {len(word_set)} слов и {len(pron_dict)} произношений")
    
    # Ищем решения головоломки
    print("Поиск слов-решений...")
    solutions = find_puzzle_words(word_set, pron_dict)
    
    # Выводим результаты
    if solutions:
        print(f"\nНайдено {len(solutions)} слов-решений:")
        for word in solutions:
            print(f"  - {word}")
            
            # Для наглядности покажем, какие омофоны получаются
            word_upper = word.upper()
            word_no_first = word[1:]
            word_no_second = word[0] + word[2:]
            
            print(f"    Исходное слово: {word} ({pron_dict[word_upper]})")
            print(f"    Без 1-й буквы:  {word_no_first} ({pron_dict[word_no_first.upper()]})")
            print(f"    Без 2-й буквы:  {word_no_second} ({pron_dict[word_no_second.upper()]})")
            print()
    else:
        print("\nСлов-решений не найдено.")
        print("Это может означать, что в тестовых данных нет реального решения.")
        print("С реальным словарём CMU результат будет другим.")

if __name__ == "__main__":
    main()