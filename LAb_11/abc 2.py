from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def display_name(self):
        print(f"Shape: {self.name}")

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(10, 5)

# Displaying information and calling abstract methods
shapes = [circle, rectangle]
for shape in shapes:
    shape.display_name()
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}\n")
