fin = open('chapter_9/word.txt')

for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)

         

