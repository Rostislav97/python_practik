def read_file(filename):
    """Читает файл и возвращает список слов"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            # Убираем знаки препинания (можно добавить больше символов)
            for char in '.,!?;:()[]{}""''':
                text = text.replace(char, '')
            # Приводим к нижнему регистру (чтобы "Кот" и "кот" считались одним словом)
            text = text.lower()
            words = text.split()
        return words
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        return []

def build_markov_chain(words, prefix_length=2):
    """
    Строит цепь Маркова
    Возвращает словарь: {префикс: список суффиксов}
    """
    if len(words) <= prefix_length:
        print("Слишком мало слов для построения цепи Маркова!")
        return {}
    
    markov_chain = {}
    
    for i in range(len(words) - prefix_length):
        # Создаем префикс как кортеж (чтобы можно было использовать как ключ словаря)
        prefix = tuple(words[i:i + prefix_length])
        suffix = words[i + prefix_length]
        
        # Добавляем суффикс к префиксу
        if prefix in markov_chain:
            markov_chain[prefix].append(suffix)
        else:
            markov_chain[prefix] = [suffix]
    
    return markov_chain

def print_statistics(markov_chain):
    """Выводит статистику по построенной цепи"""
    print(f"\n{'='*50}")
    print("СТАТИСТИКА ЦЕПИ МАРКОВА")
    print(f"{'='*50}")
    print(f"Всего уникальных префиксов: {len(markov_chain)}")
    
    # Считаем общее количество суффиксов
    total_suffixes = sum(len(suffixes) for suffixes in markov_chain.values())
    print(f"Всего связей (префикс→суффикс): {total_suffixes}")
    
    # Находим префикс с наибольшим количеством вариантов
    if markov_chain:
        max_prefix = max(markov_chain.items(), key=lambda x: len(x[1]))
        print(f"\nПрефикс с наибольшим количеством вариантов:")
        print(f"  {' '.join(max_prefix[0])} → {len(max_prefix[1])} вариантов")
        print(f"  Примеры: {max_prefix[1][:5]}")

def test_different_prefixes(words):
    """Тестирует разные длины префиксов"""
    for length in [1, 2, 3]:
        print(f"\n{'='*50}")
        print(f"ТЕСТ С ПРЕФИКСОМ ДЛИНЫ {length}")
        print(f"{'='*50}")
        chain = build_markov_chain(words, length)
        print_statistics(chain)

def main():
    # Имя файла с текстом
    filename = "text.txt"
    
    # Читаем файл
    print("Читаем файл...")
    words = read_file(filename)
    
    if not words:
        return
    
    print(f"Прочитано слов: {len(words)}")
    print(f"Первые 20 слов: {' '.join(words[:20])}")
    
    # Строим цепь Маркова с префиксом длины 2
    prefix_length = 2
    markov_chain = build_markov_chain(words, prefix_length)
    
    # Выводим статистику
    print_statistics(markov_chain)
    
    # Показываем примеры для нескольких префиксов
    print(f"\n{'='*50}")
    print("ПРИМЕРЫ ПРЕФИКСОВ И ИХ СУФФИКСОВ")
    print(f"{'='*50}")
    
    # Берем первые 5 префиксов для примера
    count = 0
    for prefix, suffixes in markov_chain.items():
        if count < 5:
            prefix_text = ' '.join(prefix)
            print(f"\nПрефикс: '{prefix_text}'")
            print(f"Суффиксы: {suffixes[:7]}")  # показываем первые 7 суффиксов
            if len(suffixes) > 7:
                print(f"  ... и еще {len(suffixes) - 7}")
            count += 1
    
    # Спрашиваем, хочет ли пользователь протестировать другие длины
    answer = input("\nХотите протестировать другие длины префиксов? (да/нет): ")
    if answer.lower() in ['да', 'yes', 'y', 'д']:
        test_different_prefixes(words)

if __name__ == "__main__":
    main()