def has_duplicates(lst):
    seen = {}  # создаем словарь внутри функции
    for item in lst:
        if item in seen:  # проверяем, есть ли элемент в словаре
            return True
        seen[item] = True  # добавляем элемент в словарь
    return False
    