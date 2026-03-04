def is_power(a, b):
    # Базовый случай: любое число в степени 0 = 1
    if a == 1:
        return True
    # Базовый случай: если a меньше b и не равно 1, то не степень
    if a < b:
        return False
    # Если a не делится на b нацело, то не степень
    if a % b != 0:
        return False
    # Рекурсивно проверяем a/b
    return is_power(a // b, b)

print(is_power(3, 3))