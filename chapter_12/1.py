def most_frequent(text):
    t = dict()
    for c in text:
        if c not in t:
            t[c] = 1
        else:
            t[c] = t[c] + 1

    # Превращаем словарь в список пар и сортируем
    items = list(t.items())  # [('а', 2), ('с', 1), ...]
    
    # Сортируем по второму элементу (частоте) в обратном порядке
    items.sort(key=lambda x: x[1], reverse=True)


print(most_frequent("строкаа"))


    
