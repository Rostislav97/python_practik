import math

def check_fermat(a, b, c, n):
    abn = a**n + b**n
    cn = c**n
    if n > 2 and a !=0 and  b != 0 and  c != 0:
        if abn == cn:
            print('Не может быть, Ферма ошибся!')
        else:
            print('Нет, это не работает') 
    else:
            print('Теорема Ферма гласит, что для любого натурального числа n > 2 уравнение не имеет решений в целых ненулевых числах a, b, c') 
    
def input_check_fermat():
     print("Введите значения:\n") 
     a = int(input('a =  '))
     b = int(input('b =  '))
     c = int(input('c =  '))
     n = int(input('n =  '))
     check_fermat(a, b, c, n)
    

    
input_check_fermat()
