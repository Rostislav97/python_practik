# Проверяет ТОЛЬКО ПЕРВУЮ букву
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

# Всегда возвращает строку 'True', игнорируя входные данные
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():  # всегда True
            return 'True'  # возвращает строку, не булево
        else:
            return 'False'

# Проверяет ТОЛЬКО ПОСЛЕДНЮЮ букву
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag  # возвращает результат только для последнего символа

# РАБОТАЕТ ПРАВИЛЬНО! Проверяет, есть ли ХОТЯ БЫ ОДНА строчная буква
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()  # flag становится True при первой строчной букве
    return flag

# Проверяет, ВСЕ ли буквы строчные (all, а не any)
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False  # нашли букву в верхнем регистре
    return True  # все буквы в нижнем регистре