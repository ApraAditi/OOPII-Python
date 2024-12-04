class Animal:
    def sound(self):
        return "Some generic sound"
class Dog(Animal):
    def sound(self): #Method overriding
        return "Bark!"
dog = Dog()
print(dog.sound()) #"Bark!" overrides "Some generic sound"


class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the parent's __init__ to initialize the name
        self.age = age

parent1 = Parent("Alice")
child1 = Child("Bob", 10)

print(parent1.name)  # Output: Alice
print(child1.name)  # Output: Bob (inherited from Parent)
print(child1.age)  # Output: 10