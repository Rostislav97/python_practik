def group_by_length(words):
    by_length = {}
    for word in words:
        length = len(word)
        if length not in by_length:
            by_length[length] = []
        by_length[length].append(word)
    return by_length


def create_masks(word):
    masks = []
    for i in range(len(word)):           # первая позиция для замены
        for j in range(i+1, len(word)):   # вторая позиция (чтобы не повторяться)
            # Создаем список букв, заменяя i и j на None
            mask_chars = []
            for pos, letter in enumerate(word):
                if pos == i or pos == j:
                    mask_chars.append(None)  # помечаем позиции замены
                else:
                    mask_chars.append(letter)
            masks.append(tuple(mask_chars))
    return masks

        
def find_metagrams(words):
    by_length = group_by_length(words)
    results = []
    
    for length, words_list in by_length.items():
        # Словарь: маска -> список слов
        mask_dict = {}
        
        for word in words_list:
            masks = create_masks(word)
            for mask in masks:
                if mask not in mask_dict:
                    mask_dict[mask] = []
                mask_dict[mask].append(word)
        
        # Ищем маски, под которые подходит ровно 2 слова
        for mask, matched_words in mask_dict.items():
            if len(matched_words) == 2:
                # Проверяем, действительно ли они различаются ровно в двух позициях
                word1, word2 = matched_words
                differences = sum(1 for a, b in zip(word1, word2) if a != b)
                if differences == 2:
                    results.append((word1, word2))
    
    return results