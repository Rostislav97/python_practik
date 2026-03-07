import math

def mysqrt(a):
    x = 3
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < 0.00000000000001:
            return y
        x = y 

def test_square_root(a):
    print("a   mysqrt(a)   math.sqrt(a)   diff\n")
    my_result = mysqrt(a)
    math_result = math.sqrt(a)
    diff = abs(my_result - math_result)
    print(f"{a} {my_result} {math_result} {diff}")

test_square_root(16)
