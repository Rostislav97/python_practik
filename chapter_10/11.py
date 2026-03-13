#6.4 миллиарда сравнений, нужна оптимизация


word_list = []
with open('chapter_9/word.txt') as fin:
    for line in fin:
        word_list.append(line.strip())


def reverce_pair(word_list):
    pairs = []
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):  # начинаем с i+1, чтобы не сравнивать слово с самим собой
            if len(word_list[i]) == len(word_list[j]):  # сначала проверяем длину
                if word_list[i] == word_list[j][::-1]:
                    pairs.append((word_list[i], word_list[j]))
    return pairs

print(reverce_pair(word_list))