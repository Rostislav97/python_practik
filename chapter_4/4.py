import math
import turtle
bob = turtle.Turtle()


def draw_a(t, leight):
    t.lt(-75)
    t.bk(leight)
    t.rt(-150)
    t.bk(leight)
    t.rt(180)
    t.bk(leight/2)
    t.lt(-75)
    t.bk(leight/4)

draw_a(bob, 60)

turtle.mainloop()