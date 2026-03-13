def invert_dict(d):
    inverse = {}
    for key, val in d.items():  # .items() дает сразу пары ключ-значение
        inverse.setdefault(val, []).append(key)
    return inverse


# Пример работы setdefault:
d = {}
value = d.setdefault('a', [])  # ключа 'a' нет → создает 'a': [] и возвращает []
print(d)  # {'a': []}

value.append(1)  # работаем с полученным списком
print(d)  # {'a': [1]}