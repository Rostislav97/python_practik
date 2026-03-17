import random

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def choose_from_hist(s):
    hist = histogram(s)
    #создаем из гистограммы обратно список, где каждая буква будет повторятся столько сколько указано в гистрограмме
    spisok = []
    for key, value in hist.items():
        spisok.extend[[key] * value]
    
    return random.choice(spisok)


