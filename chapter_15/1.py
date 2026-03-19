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



# Создаем центр круга
p_centre = Point(150, 100)
# Создаем круг
c = Circle(p_centre, 75)

# Создаем точку для проверки
p = Point(100, 100)

#cоздаем прямоугольник
figure = Rectangle(100,200,p)

def point_in_circle(circle, point):
    # circle.center - это центр круга (объект Point)
    dx = point.x - circle.center.x
    dy = point.y - circle.center.y
    distance = (dx**2 + dy**2) ** 0.5
    return distance <= circle.radius



def rect_in_circle(circle, rectangle):
    # Получаем левый верхний угол
    corner = rectangle.corner
    
    # 1. Проверяем левый верхний угол
    if not point_in_circle(circle, corner):
        return False
    
    # 2. Проверяем правый верхний угол
    p2 = Point(corner.x + rectangle.width, corner.y)
    if not point_in_circle(circle, p2):
        return False
    
    # 3. Проверяем правый нижний угол
    p3 = Point(corner.x + rectangle.width, corner.y - rectangle.height)
    if not point_in_circle(circle, p3):
        return False
    
    # 4. Проверяем левый нижний угол
    p4 = Point(corner.x, corner.y - rectangle.height)
    if not point_in_circle(circle, p4):
        return False
    
    # Если все углы прошли проверку
    return True
