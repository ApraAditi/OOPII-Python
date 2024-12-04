# Base class
class UniversityMember:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def introduce(self):
        raise NotImplementedError("Subclass must implement this method")

# Derived class - Student
class Student(UniversityMember):
    def __init__(self, name, id, major):
        super().__init__(name, id)
        self.major = major

    def introduce(self):
        return f"Hello, I am {self.name}, a student majoring in {self.major}. My ID is {self.id}."

# Derived class - Professor
class Professor(UniversityMember):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def introduce(self):
        return f"Hello, I am  {self.name}, a professor in the {self.department} department. My ID is {self.id}."

# Function to demonstrate polymorphism
def member_introduction(member):
    print(member.introduce())

# Creating objects of Student and Professor
student = Student("Apra Das", "1823", "Computer Science and Engineering")
professor = Professor("Nasima Islam Bithi", "23456", "Computer Science and Engineering")

# Demonstrating polymorphism by calling the introduce method on different objects
member_introduction(student)
member_introduction(professor)
