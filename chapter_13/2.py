import string

def process_book(filename):
    """Читает книгу, очищает слова и считает их количество"""
    
    # Открываем файл
    fin = open(filename, 'r')
    
    # Пропускаем строки до маркера начала книги
    marker = "START OF THIS PROJECT GUTENBERG EBOOK"
    start_reading = False
    
    word_counter = {}
    total_words = 0
    
    # Читаем файл построчно
    for line in fin:
        # Ищем маркер начала книги
        if not start_reading and marker in line:
            start_reading = True
            continue  # пропускаем саму строку с маркером
        
        # Если уже начали читать книгу
        if start_reading:
            # Убираем пробелы в начале и конце строки
            line = line.strip()
            
            # Разбиваем строку на слова
            words = line.split()
            
            # Обрабатываем каждое слово
            for word in words:
                total_words += 1  # считаем общее количество
                
                # Очищаем слово от знаков препинания
                clean_word = ""
                for char in word:
                    if char not in string.punctuation:
                        clean_word = clean_word + char
                
                # Преобразуем в нижний регистр
                clean_word = clean_word.lower()
                
                # Если слово не пустое, считаем его
                if clean_word != "":
                    if clean_word not in word_counter:
                        word_counter[clean_word] = 1
                    else:
                        word_counter[clean_word] += 1
    
    # Закрываем файл
    fin.close()
    
    return word_counter, total_words

# Используем функцию
word_counts, total = process_book('chapter_9/book.txt')

# Выводим результаты
print(f"Всего слов в книге: {total}")
print(f"Уникальных слов: {len(word_counts)}")
print(f"Соотношение уникальных/общее: {len(word_counts)/total:.2%}")

# Для сравнения книг можно вызвать функцию несколько раз
# counts_book1, total1 = process_book('book1.txt')
# counts_book2, total2 = process_book('book2.txt')