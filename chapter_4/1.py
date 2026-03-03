import math
import turtle

def square(t, length):
    """Draws a square with sides of the given length."""
    print(f'--> Начинаем square с length={length}')
    for i in range(4):
        t.fd(length)
        t.lt(90)
    print(f'<-- Заканчиваем square')

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
    bob.speed(1)  # замедлим черепашку, чтобы видеть процесс
    
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    
    circle(bob, radius)
    
    turtle.mainloop()