#Было
def print_n(s, n):
    while n <= 0:
        print(s)
        print_n(s, n-1)
    return

#Cтало
def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1
    # здесь функция автоматически завершается
    