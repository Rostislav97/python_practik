import math

def eval_loop():
    while True:
        arg = input("Введите выражение:  ")
        if arg == 'готово':
            break
        else:
           result = eval(arg)
           print(result)
    print('Готово!')



eval_loop()