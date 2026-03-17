import imported_for_2
import shelve

def store_anagrams():
    try:
        shelf = shelve.open('my_data', 'c')
        shelf['anagrams'] = imported_for_2.slovar
        shelf.close()
    except:
        print('Что-то пошло не так при чтении и записи файлов.') 



def read_anagrams(word):  # функция принимает слово
    try:
        with shelve.open('my_data', 'r') as shelf:
            anagrams_dict = shelf['anagrams'] # достаем словарь
            
            # 1. Сортируем буквы переданного слова
            key = tuple(sorted(word))  # тот же ключ, что и в словаре
            
            # 2. Проверяем, есть ли такой ключ в словаре
            if key in anagrams_dict:
                return anagrams_dict[key]  # возвращаем список анаграмм
            else:
                return []  # если нет анаграмм, возвращаем пустой список
            
    except:
        print('Что-то пошло не так при чтении и записи файлов.') 

    