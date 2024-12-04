class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class PermanentEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def print_details(self):
        print("Permanent Employee:")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Salary: {self.calculate_salary()}")

class ContractEmployee(Employee):
    def __init__(self, name, id, hourly_rate, hours_worked):
        super().__init__(name, id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def print_details(self):
        print("Contract Employee:")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Salary: {self.calculate_salary()}")

permanent_employee = PermanentEmployee("Apra", 1823, 5000)
contract_employee = ContractEmployee("Aditi", 3456, 20, 150)

permanent_employee.print_details()
contract_employee.print_details()