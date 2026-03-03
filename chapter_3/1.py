def right_justify(s):
    x = 70 - len(s)
    stroka = x * " "
    y = stroka + s
    print(y)

right_justify('monty')
    