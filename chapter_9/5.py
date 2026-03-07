def uses_all(word, required):
    for letter in required:  # проходим по обязательным буквам
        if letter not in word:  # если обязательной буквы нет в слове
            return False
    return True  # все обязательные буквы есть