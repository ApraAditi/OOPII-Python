# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

# Derived class - Dog
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class - Cat
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Function to demonstrate polymorphism
def animal_speak(animal):
    print(animal.speak())

# Creating objects of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak method on different objects
animal_speak(dog)  # Output: Buddy says Woof!
animal_speak(cat)  # Output: Whiskers says Meow!
