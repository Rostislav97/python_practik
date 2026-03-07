def has_no_e(word):
    for c in word:
        if c == 'e':
            return False  # нашли e - сразу возвращаем False
    return True  # проверили все буквы, e не нашли
        
fin = open('chapter_9/word.txt')

for line in fin:
    words = line.strip()
    if has_no_e(words) == True :
        print(words)
        
print(has_no_e("abce"))
