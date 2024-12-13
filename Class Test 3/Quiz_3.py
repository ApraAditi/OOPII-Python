from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, StudentID, Name):
        self._StudentID = StudentID
        self._Name = Name
        self._TuitionFee = 0
        
    def get_StudentID(self):
        return self._StudentID
    
    def get_Name(self):
        return self._Name
    
    def get_TuitionFee(self):
        return self._TuitionFee
    
    @abstractmethod
    def CalculateFee(self):
        pass
    
class UndergraduateStudent(Student):
    def __init__(self, StudentID, Name, CreditHour):
        super().__init__(StudentID, Name)
        self.__CreditHour = CreditHour
        
    def get_CreditHour(self):
        return self.__CreditHour
        
    def set_CreditHour(self, CreditHour):
        self.__CreditHour = CreditHour
        
    def CalculateFee(self):
        if self.__CreditHour < 0:
            raise ValueError("Credit Hour can't be Negative.")
        self._TuitionFee = self.__CreditHour * 150
        return self._TuitionFee
     
class GraduateStudent(Student):
    def __init__(self, StudentID, Name, ResearchFee):
        super().__init__(StudentID, Name)
        self.__ResearchFee = ResearchFee
        
    def get_ResearchFee(self):
        return self.__ResearchFee
        
    def set_ResearchFee(self, ResearchFee):
        self.__ResearchFee = ResearchFee
            
    def CalculateFee(self):
        if self.__ResearchFee < 0:
            raise ValueError("Research Fee must be Positive.")
        self._TuitionFee = self.__ResearchFee + 3000
        return self._TuitionFee
            
def main():
    print("Welcome to the Student Management System!")
    
    while True:
        student_type = input("Enter student type (undergraduate/graduate) or 'exit' to quit: ").strip().lower()
        
        if student_type == 'exit':
            break
        
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        
        if student_type == 'undergraduate':
            try:
                credit_hour = int(input("Enter Credit Hours: "))
                undergrad_student = UndergraduateStudent(student_id, name, credit_hour)
                undergrad_fee = undergrad_student.CalculateFee()
                print(f"\n\nUndergraduate Student Details")
                print(f"\nStudent ID: {undergrad_student.get_StudentID()}")
                print(f"Name: {undergrad_student.get_Name()}")
                print(f"Tuition Fee: {undergrad_student.get_TuitionFee()}")
            except ValueError as e:
                print(e)
        
        elif student_type == 'graduate':
            try:
                research_fee = int(input("Enter Research Fee: "))
                grad_student = GraduateStudent(student_id, name, research_fee)
                grad_fee = grad_student.CalculateFee()
                print(f"\n\nGraduate Student Details")
                print(f"\nStudent ID: {grad_student.get_StudentID()}")
                print(f"Name: {grad_student.get_Name()}")
                print(f"Tuition Fee: {grad_student.get_TuitionFee()}")
            except ValueError as e:
                print(e)
        
        else:
            print("Invalid student type. Please enter 'undergraduate' or 'graduate'.")

if __name__ == "__main__":
    main()