def is_reverse(age1, age2):
    """Проверяет, является ли age1 перевернутым age2"""
    # zfill(2) добавляет ноль слева для однозначных чисел (3 → "03")
    return str(age1).zfill(2) == str(age2).zfill(2)[::-1]

def check_pair(son, mom):
    """Проверяет пару возрастов и считает совпадения"""
    count = 0
    matches = []
    
    # Проверяем от момента рождения сына до его старости
    for diff in range(0, 80):  # смотрим 80 лет вперед
        future_son = son + diff
        future_mom = mom + diff
        
        if future_mom > 100 or future_son > 100:
            break
            
        if is_reverse(future_son, future_mom):
            count += 1
            matches.append((future_son, future_mom))
    
    return count, matches

# Основной поиск
for son in range(10, 70):  # сыну от 10 до 70
    for mom in range(son + 15, 100):  # мать старше минимум на 15 лет
        
        count, matches = check_pair(son, mom)
        
        if count == 8:  # должно быть 8 совпадений за всю жизнь
            print(f"НАШЛИ! Сейчас сыну {son}, матери {mom}")
            print("Совпадения возрастов (сын, мать):")
            for s, m in matches:
                print(f"  {s} и {m} → {s}{m} и {m}{s}")
            print()