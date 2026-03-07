def rotate_word(word, n):
    result = ""  # сюда собираем результат
    for c in word:
        if 'а' <= c <= 'я':  # если русская строчная буква
            position = ord(c) - ord('а') 
            new_position = (position +  n) % 33
            new_bukva = chr(ord('а') + new_position)
            result = result + new_bukva
        elif 'А' <= c <= 'Я': # обработка заглавных (используй ord('А') как базовую точку)
            position = ord(c) - ord('а') 
            new_position = (position +  n) % 33
            new_bukva = chr(ord('а') + new_position)
            result = result + new_bukva
        else:
            result = result + c  # не буквы оставляем как есть
    print(result)





rotate_word("Король", 2)