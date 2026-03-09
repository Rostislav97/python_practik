def has_duplicates(t):
    # Сравниваем каждый элемент с каждым
    for i in range(len(t)):        # i это индекс: 0, 1, 2, 3...
        for j in range(i + 1, len(t)):  # j это индекс: i+1, i+2...
            if t[i] == t[j]:       # если элементы равны
                return True        # нашли дубликат!
    return False                    # проверили все - дубликатов нет