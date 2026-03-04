import math

def sravnenie(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

#print(sravnenie(2, 1))


def hypotenuse(x, y):
    #формула гипотенузы c = √(a² + b²)
    #считаем простое выражение
    c = (x**2) + (y**2)
    result =  math.sqrt(c)
    return result

#print(hypotenuse(2, 5))

def  is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False
    
print(is_between(2, 2, 2))