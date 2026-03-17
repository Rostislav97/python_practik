fin = open('chapter_9/word.txt')
slovar = dict()

def spisok_annogram(fin):
    for line in fin:
        word = line.strip()
        # Сортируем буквы и делаем кортеж
        key_slovar = tuple(sorted(word))
        
        # Добавляем слово в словарь
        if key_slovar not in slovar:
            slovar[key_slovar] = [word]
        else:
            slovar[key_slovar].append(word)
    
    return slovar

# Вызываем функцию
result = spisok_annogram(fin)
fin.close()  # не забываем закрыть файл