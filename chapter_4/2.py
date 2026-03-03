import math
import turtle

def polyline(t, n, length, angle):
    """Draws n line segments."""
    print(f'--> Начинаем polyline: n={n}, length={length:.1f}, angle={angle:.1f}°')
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    print(f'<-- Заканчиваем polyline')    

def polygon(t, n, length):
    """Draws a polygon with n sides."""
    print(f'--> Начинаем polygon: n={n}, length={length}')
    angle = 360.0/n
    polyline(t, n, length, angle)
    print(f'<-- Заканчиваем polygon')

def arc(t, r, angle):
    """Draws an arc with the given radius and angle."""
    print(f'--> Начинаем arc: r={r}, angle={angle}°')
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    print(f'    arc_length={arc_length:.1f}, n={n}, step_length={step_length:.1f}, step_angle={step_angle:.1f}°')
    
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)
    print(f'<-- Заканчиваем arc')


def circle(t, r):
    """Draws a circle with the given radius."""
    print(f'--> Начинаем circle: r={r}')
    arc(t, r, 360)
    print(f'<-- Заканчиваем circle')

if __name__ == '__main__':
    bob = turtle.Turtle()
    #bob.speed(15)  # замедлим черепашку, чтобы видеть процесс
    
    radius = 100
    bob.pu()
    bob.lt(90)
    bob.pd()
    
def lepestok(t, r, angle):
    
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def flower(t, n, r, angle):
    """Рисует цветок с n лепестками"""
    for i in range(n):
        lepestok(t, r, angle)  # рисуем лепесток
        t.lt(360.0/n)       # поворачиваем к следующему лепестку
    
flower(bob, 7, 50, 90)
    
turtle.mainloop()