def nested_sum(t):
    total = 0                    # Переменная для накопления суммы
    for sublist in t:            # sublist это [1,2], потом [3], потом [4,5,6]
        for number in sublist:   # Проходим по каждому числу внутри sublist
            total = total + number  # Добавляем число к общей сумме
    return total

print(nested_sum([[1, 2], [3], [4, 5, 6]]))