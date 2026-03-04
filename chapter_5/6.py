import turtle
bob = turtle.Turtle()

def Koch(t, x):
    if x >= 3:
        leight = x / 3
        angle = 60
        Koch(t, leight)
        t.lt(angle)
        Koch(t, leight)
        t.rt(angle*2)
        Koch(t, leight)
        t.lt(angle)
        Koch(t, leight)
    else:
        t.fd(x)

Koch(bob, 90)
turtle.mainloop()