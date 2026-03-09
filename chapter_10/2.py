def cumsum(t):
    result = []          # новый список для результата
    total = 0            # переменная для накопления суммы
    
    for с in t:      # проходим по каждому числу
        total = с + total      # добавляем текущее число к сумме
        result.append(total)  # добавляем текущую сумму в результат
    
    return result


print(cumsum([1, 2, 3]))