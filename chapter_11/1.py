fin = open('chapter_9/words.txt')
slovar = dict()  # создаем словарь ДО цикла

for line in fin:
    word = line.strip()  # получаем слово из строки
    slovar[word] = True  # добавляем слово как ключ

print(slovar)  # посмотрим что получилось
