import math

class Shape:
    def area(self):
        """Raises NotImplementedError to indicate derived classes should override this method."""
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initializes a Rectangle instance with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initializes a Circle instance with radius."""
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * self.radius ** 2


