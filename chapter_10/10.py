import bisect

def in_bisect(sorted_list, target):
    """Возвращает индекс target в отсортированном списке или none, если не найден"""
    pos = bisect.bisect_left(sorted_list, target)
    if pos < len(sorted_list) and sorted_list[pos] == target:
        return pos
    return None

# Использование:
# Читаем файл ОДИН раз
word_list = []
with open('chapter_9/word.txt') as fin:
    for line in fin:
        word_list.append(line.strip())

# Теперь можно много раз искать слова
print(in_bisect(word_list, 'python'))
print(in_bisect(word_list, 'hello'))