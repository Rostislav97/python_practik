def is_triangle(a, b, c):
    if a+b < c and a+c < b and  c+b < a :
        print('Нет')
    else:
        print('Да') 
    
    
def input_check_triangle():
     print("Введите значения:\n") 
     a = int(input('a =  '))
     b = int(input('b =  '))
     c = int(input('c =  '))
     
     is_triangle(a, b, c)

input_check_triangle()