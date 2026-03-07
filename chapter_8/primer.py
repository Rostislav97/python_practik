""" def text(str):
    length = len(str)
    index = -1
    while index >= -length:
        letter = str[index]
        print(letter)
        index = index - 1 """


""" prefixes = 'БВККЛМНШ'
index = 0

for letter in prefixes:
    if index == 0 or index == 1 or index == 3:
        print(letter + 'ряк')
    elif index == 2:
        print(letter + 'вяк')
    elif index == 7:
        print(letter + 'мяк')
    else:
        print(letter + 'як')
    
    index += 1 """

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


print(find("корабль", "а", 1))

