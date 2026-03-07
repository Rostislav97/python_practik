import math

def estimate_pi():
    # Константа перед суммой
    constant = (2 * math.sqrt(2)) / 9801
    
    total = 0  # сумма
    k = 0
    while True:
        # Вычисляем числитель: (4k)! * (1103 + 26390*k)
        numerator = math.factorial(4*k) * (1103 + 26390*k)
        
        # Вычисляем знаменатель: (k!)^4 * 396^(4k)
        denominator = (math.factorial(k))**4 * (396**(4*k))
        
        # Текущий член суммы
        term = numerator / denominator
        
        # Добавляем к общей сумме
        total += term
        
        # Если член стал очень маленьким - выходим
        if term < 1e-15:
            break
            
        k += 1
    
    # Получаем 1/π
    one_over_pi = constant * total
    
    # Возвращаем π
    return 1 / one_over_pi

print("Мой π:", estimate_pi())