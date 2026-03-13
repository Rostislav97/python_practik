import bisect

# Оригинальный список (в том порядке, как в файле)
original_words = []
with open('chapter_9/word.txt') as fin:
    for line in fin:
        original_words.append(line.strip())
 
# Создаем отсортированную копию для бинарного поиска
sorted_words = sorted(original_words)

def in_bisect(sorted_list, target):
    pos = bisect.bisect_left(sorted_list, target)
    return pos < len(sorted_list) and sorted_list[pos] == target

def find_interlock_pairs():
    pairs = []
    
    for word in original_words:  # проходим по оригинальному списку
        if len(word) < 2:
            continue
            
        first = word[0::2]
        second = word[1::2]
        
        # Используем отсортированный список для поиска
        if in_bisect(sorted_words, first) and in_bisect(sorted_words, second):
            # Дополнительная проверка: не является ли слово комбинацией самого себя?
            if first != second or word.count(first[0]) > 1:  # избегаем самоповторов
                pairs.append((first, second, word))
    
    return pairs

result = find_interlock_pairs()
print(f"Найдено пар: {len(result)}")