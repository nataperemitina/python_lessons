"""
Модуль вычисления площадей геометрических фигур.
"""
from math import pi as PI

# Только то, что объявлено в __all__ будет видно по from *
__all__ = [
    'calculate_square_area',
    'calculate_rectangle_area',
    'calculate_triangle_area',
    'calculate_circle_area',
]

def calculate_square_area(a):
    """Возвращает площадь квадрата."""
    return a ** 2


def calculate_rectangle_area(a, b):
    return a * b


def calculate_triangle_area(a, b, c):
    """Формула Герона"""
    p = (a + b + c)/2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def calculate_circle_area(r):
    return PI * r ** 2
