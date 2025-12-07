import math


class Shape:
    """Base class for shapes. Subclasses must implement area()."""

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    """Rectangle shape with length and width."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    """Circle shape with radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
