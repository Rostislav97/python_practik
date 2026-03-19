import turtle
bob = turtle.Turtle()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center  # ссылка на Point
        self.radius = radius

class Rectangle: #Определяет прямоугольник. атрибуты: width, height, corner.
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner   

# Создаем точку для проверки
p = Point(100, 100)

#cоздаем прямоугольник
figure = Rectangle(100,200,p)

def draw_rect(t, rectangle):
    # t - это черепашка (объект Turtle)
    # rectangle - это наш прямоугольник
    
    # 1. Поднимаем перо (чтобы не рисовать лишнего)
    t.penup()
    
    # 2. Идем в левый верхний угол
    corner = rectangle.corner
    t.goto(corner.x, corner.y)
    
    # 3. Опускаем перо (начинаем рисовать)
    t.pendown()
    
    # 4. Рисуем прямоугольник по часовой стрелке:
    # Левый верхний -> Правый верхний
    t.goto(corner.x + rectangle.width, corner.y)
    
    # Правый верхний -> Правый нижний
    t.goto(corner.x + rectangle.width, corner.y - rectangle.height)
    
    # Правый нижний -> Левый нижний
    t.goto(corner.x, corner.y - rectangle.height)
    
    # Левый нижний -> обратно в левый верхний (замыкаем)
    t.goto(corner.x, corner.y)



draw_rect(bob, figure)

turtle.mainloop()