def is_anagram(t):
    word1 = t[0]
    word2 = t[1]
    if len(word1) != len(word2):
        return False
    else:
        for letter in word1:
            if word1.count(letter) != word2.count(letter):
                return False
        return True
    


#Более короткое решение

def is_anagram2(t):
    return sorted(t[0]) == sorted(t[1])
