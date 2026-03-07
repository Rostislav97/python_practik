def has_three_doubles(word):
    i = 0
    while i < len(word) - 5:  # Останавливаемся, чтобы i+5 существовал
        if (word[i] == word[i+1] and
            word[i+2] == word[i+3] and
            word[i+4] == word[i+5]):
            return True
        i += 1  # ВАЖНО: увеличиваем i!
    return False

#но лучше использовать for
def has_three_bles(word):
    for i in range(len(word) - 5):
        if (word[i] == word[i+1] and
            word[i+2] == word[i+3] and
            word[i+4] == word[i+5]):
            return True
    return False

fin = open('chapter_9/word.txt')

for line in fin:
    word = line.strip()
    if has_three_doubles(word):
        print(word)

fin.close()




