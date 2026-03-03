import turtle

def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    theta = 0.0  # текущий угол (суммарный поворот от начала)
    
    for i in range(n):
        t.fd(length)  # делаем шаг вперед
        
        # САМАЯ ВАЖНАЯ ЧАСТЬ: вычисляем, на сколько повернуть
        dtheta = 1 / (a + b * theta)  # угол поворота на этом шаге
        
        t.lt(dtheta)  # поворачиваем
        theta += dtheta  # запоминаем общий поворот

bob = turtle.Turtle()
draw_spiral(bob, n=1000)

turtle.mainloop()