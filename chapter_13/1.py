import string

def read_file():
    # Открываем файл
    fin = open('chapter_9/word.txt', 'r')
    
    # Читаем файл построчно
    for line in fin:
        # Убираем пробелы в начале и конце строки
        line = line.strip()
        
        # Разбиваем строку на слова (по пробелам)
        words = line.split()
        
        # Обрабатываем каждое слово
        for word in words:
            # Очищаем слово от знаков препинания
            clean_word = ""
            
            # Проходим по каждому символу в слове
            for char in word:
                # Если символ не является знаком препинания
                if char not in string.punctuation:
                    # Добавляем его к очищенному слову
                    clean_word = clean_word + char
            
            # Преобразуем в нижний регистр
            clean_word = clean_word.lower()
            
            # Если слово не пустое, печатаем его
            if clean_word != "":
                print(clean_word)
    
    # Закрываем файл
    fin.close()

# Вызываем функцию
read_file()
