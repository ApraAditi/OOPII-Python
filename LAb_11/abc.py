from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def display_info(self):
        print(f"Animal Name: {self.name}")

# Derived class - Dog
class Dog(Animal):
    def sound(self):
        return "Woof"

    def move(self):
        return "Runs"

# Derived class - Bird
class Bird(Animal):
    def sound(self):
        return "Chirp"

    def move(self):
        return "Flies"

# Creating instances of Dog and Bird
dog = Dog("Buddy")
bird = Bird("Tweety")

# Displaying information and calling abstract methods
for animal in (dog, bird):
    animal.display_info()
    print(f"Sound: {animal.sound()}")
    print(f"Movement: {animal.move()}\n")
