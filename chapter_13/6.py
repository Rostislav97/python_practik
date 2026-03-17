import string

def read_slovar(filename):
    slovar = {}
    fin = open(filename, 'r')
    for line in fin:
        # Убираем пробелы в начале и конце строки
        word = line.strip()
        if word not in slovar:
           slovar[word]= True
    
    fin.close()    
    return slovar
    

def read_book(file):
    words_slovar = {}
    book = open(file, 'r')
    # Читаем файл построчно
    for stroka in book:
        # Убираем пробелы в начале и конце строки
        stroka = stroka.strip()
        
        # Разбиваем строку на слова (по пробелам)
        words = stroka.split()
        
        # Обрабатываем каждое слово
        for letter in words:
            # Очищаем слово от знаков препинания
            clean_word = ""
            
            # Проходим по каждому символу в слове
            for char in letter:
                # Если символ не является знаком препинания
                if char not in string.punctuation:
                    # Добавляем его к очищенному слову
                    clean_word = clean_word + char
            
            # Преобразуем в нижний регистр
            clean_word = clean_word.lower()
            
            # Если слово не пустое, печатаем его
            if clean_word != "":
                if clean_word not in words_slovar:
                    words_slovar[clean_word]= True
            
        return words_slovar
        
def sravnenie(filename, file):
    slov = read_slovar(filename)
    bok = read_book(file)
    words_set1 = set(slov)
    words_set2 = set(bok)
    missing_words = words_set2 - words_set1
    
    return missing_words