"строка".метод(аргументы)
# или
переменная_с_текстом.метод(аргументы) 



Конкретные примеры:
1. strip() - чистит пробелы
python
# Проблема: в ответах сервера часто есть лишние пробелы и переносы строк
text = "  Привет, мир!  \n"
clean_text = text.strip()
print(clean_text)  # "Привет, мир!" (без пробелов и переносов)


2. lower() и upper() - регистр
python
text = "Привет Мир"
print(text.lower())  # "привет мир"
print(text.upper())  # "ПРИВЕТ МИР"


3. replace() - замена
python
text = "Я люблю кошек"
new_text = text.replace("кошек", "собак")
print(new_text)  # "Я люблю собак"

# Удаление лишних символов:
text = "Привет,\nмир!"
clean = text.replace("\n", " ")  # заменяем перенос строки на пробел
print(clean)  # "Привет, мир!"


4. find() - поиск позиции
python
text = "Привет, мир!"
position = text.find("мир")
print(position)  # 8 (индекс, где начинается "мир")

# Если не найдено:
print(text.find("кот"))  # -1


5. split() - разбить на части
python
text = "яблоко,банан,апельсин"
fruits = text.split(",")
print(fruits)  # ['яблоко', 'банан', 'апельсин']



6. in - простейшая проверка (не метод, но часто нужен)
python
text = "Вход выполнен успешно"
assert "успешно" in text  # True
assert "ошибка" not in text  # True


Цепочка методов (делаем всё сразу):
python
text = "  ПРИВЕТ, МИР!  \n"
clean = text.strip().lower().replace("!", "")
print(clean)  # "привет, мир"


Главное правило:
Методы просто возвращают новую строку, не изменяя старую:

python
text = "  ПРИВЕТ  "
clean = text.strip()
print(text)   # "  ПРИВЕТ  " (оригинал не изменился!)
print(clean)  # "ПРИВЕТ" (новая строка) 