def uses_only(word, allowed):
    for letter in word:
        if letter not in allowed:  # если буква НЕ в разрешенных
            return False
    return True  # все буквы в разрешенных