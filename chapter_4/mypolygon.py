""" import turtle
bob = turtle.Turtle()
for i in range(4):
    bob.fd(100)
    bob.lt(90)
turtle.mainloop() """

""" import turtle
bob = turtle.Turtle()

def square(t):
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)

square(bob) """

""" import turtle
bob = turtle.Turtle()

def square(t, arg):
    t.fd(arg)
    t.lt(90)
    t.fd(arg)
    t.lt(90)
    t.fd(arg)
    t.lt(90)
    t.fd(arg)

square(bob, 10) """

""" import turtle
bob = turtle.Turtle()

def polygon(t, n):
    for i in range(n):
        t.fd(100)
        t.lt(360/n)
    

polygon(bob, 10) """


""" import turtle
import math
bob = turtle.Turtle()

def polygon(t, n, l):
    for i in range(n):
        t.fd(l)
        t.lt(360/n)
    
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    l = circumference / n
    polygon(t, n, l)
    
circle(bob, 100)   """

import turtle
import math

bob = turtle.Turtle()

def polygon(t, n, length, angle):  # добавили параметр angle
    for i in range(int(n)):
        t.fd(length)
        t.lt(angle/n)  # поворачиваем на часть от нужного угла

def arc(t, r, angle):
    n = 50
    step_length = (2 * math.pi * r) / n
    steps = n * angle / 360
    polygon(t, steps, step_length, angle)  # передаем угол

arc(bob, 50, 180)