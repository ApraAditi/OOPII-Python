# Defining the Employee class
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Monthly Salary: {self.salary:.2f}")

    def give_raise(self, amount):
        if amount < 0:
            raise ValueError("Raise amount cannot be negative.")
        self.salary += amount
        print(f"{self.name} received a raise of {amount:.2f}. New monthly salary is {self.salary:.2f}")

    def annual_salary(self):
        annual_salary = self.salary * 12
        print(f"Annual Salary of {self.name} is {annual_salary:.2f}")

# Function to take employee details input
def create_employee():
    try:
        name = input("Enter the employee's name: ")
        position = input("Enter the employee's position: ")
        salary = float(input("Enter the employee's salary: "))
        return Employee(name, position, salary)
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

# Main program
if __name__ == "__main__":
    emp = create_employee()
    if emp:
        emp.display_details()
        try:
            raise_amount = float(input("Enter the raise amount: "))
            emp.give_raise(raise_amount)
        except ValueError as e:
            print(f"Invalid input for raise amount: {e}")
        
        emp.annual_salary()
