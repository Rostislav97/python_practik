fin = open('chapter_9/word.txt')

def create_spisok():
    res = []
    for line in fin:
        word = line.strip()
        res.append(word)
    return res



def create_spisok2():
    t = []
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


