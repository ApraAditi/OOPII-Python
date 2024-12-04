class Shape:
    def __init__(self, name):
        self.shape_name = name
    
    def get_name(self):
        print("The Shape is:", self.shape_name)
        
        
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")  # Using super() to call the constructor of the base class
        self.radius = radius
        
    def area(self):
        area = 3.14159 * (self.radius ** 2)
        print(f"Area of the Circle: {area:.2f}")
        
    def circumference(self):
        circumference = 2 * 3.14159 * self.radius
        print(f"Circumference of the Circle: {circumference:.2f}")
    
    def display(self):
        self.area()
        self.circumference()
        self.get_name()
    
# Creating an instance of the Circle class
C1 = Circle(5)

# Displaying the properties and calculations
C1.area()
C1.circumference()
C1.display()
