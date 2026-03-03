import math
import turtle
bob = turtle.Turtle()

def treugolnik(t, r, angle):
    for i in range(3):
        t.fd(r)
        t.lt(180-angle)

def pirog(t, r, n, angle):
    for i in range(n):
        treugolnik(t, r, angle)
        t.lt(360-angle)

pirog(bob, 60, 6, 60)

turtle.mainloop()