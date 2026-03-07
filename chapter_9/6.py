def is_abecedarian(word, index = 0):
    if index >= len(word)-1:
        return True
    else:
        if word[index] > word[index+1]:
            return False
    return is_abecedarian(word, index + 1)


print(is_abecedarian("вапвапв", index = 0))
