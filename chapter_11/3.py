memo = {}

def ack_memo(m, n):
    # Проверяем, есть ли уже результат
    if (m, n) in memo:
        return memo[(m, n)]
    
    # Вычисляем как обычно
    if m == 0:
        result = n + 1
    elif n == 0:
        result = ack_memo(m-1, 1)
    else:
        result = ack_memo(m-1, ack_memo(m, n-1))
    
    # Запоминаем результат
    memo[(m, n)] = result
    return result 