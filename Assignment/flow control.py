grades = [85, 78, 92, 45, 33, 67, 88, 41]

for grade in grades:
    if grade > 80:
        print(f"Score: {grade} - Grade: A")
    elif grade >= 60 and grade <= 80:
        print(f"Score: {grade} - Grade: B")
    elif grade >= 40 and grade < 60:
        print(f"Score: {grade} - Grade: C")
    else:
        print(f"Score: {grade} - Grade: F")
   
         
         