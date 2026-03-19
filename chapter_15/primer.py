class Point: """Представление точки в двумерном пространстве."""

# Создаем две точки
point1 = Point()
point1.x = 3.0
point1.y = 5.0

point2 = Point()
point2.x = 1.0
point2.y = 2.0

def distance_between_points(point1, point2):
    """
    Вычисляет расстояние между двумя точками.
    """
    dx = point2.x - point1.x
    dy = point2.y - point1.y
    return (dx**2 + dy**2) ** 0.5  # Квадратный корень из суммы квадратов