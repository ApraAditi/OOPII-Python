# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

    def get_name(self):
        print(f"This animal's name is {self.name}")


# Derived class - Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} says Woof!")

    def get_breed(self):
        print(f"{self.name} is a {self.breed}")


# Derived class - Cat
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print(f"{self.name} says Meow!")

    def get_color(self):
        print(f"{self.name} is {self.color} in color")


# Create instances of Dog and Cat
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")

# Demonstrate functionality
dog.get_name()
dog.get_breed()
dog.speak()

cat.get_name()
cat.get_color()
cat.speak()
