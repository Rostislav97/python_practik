def avoids(word, xui):
    if len(word) == 0:
        return False
    if word[0] in xui:
        return True
    return avoids(word[1:], xui)

fin = open('chapter_9/word.txt')

xui = input("Введите строку запрещенных букв  ")

for line in fin:
    words = line.strip()
    if avoids(words, xui) == False :
        print(words)


