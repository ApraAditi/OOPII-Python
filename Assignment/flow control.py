grades = [85, 78, 92, 45, 33, 67, 88, 41]

#a. categorize each student's grade
for grade in grades:
    if grade > 80:
        print(f"Score: {grade} - Grade: A")
    elif grade >= 60 and grade <= 80:
        print(f"Score: {grade} - Grade: B")
    elif grade >= 40 and grade < 60:
        print(f"Score: {grade} - Grade: C")
    else:
        print(f"Score: {grade} - Grade: F")
   
 #b. boost_grades        
def boost_grades(grade):
    return grade * 1.05
boosted_grades = list(map(boost_grades, grades))
print("\nBoosted Grades: ",boosted_grades)

#c. Use a lambda function
high_grades = list(filter(lambda grade: grade >  90, boosted_grades))
print("\nBoosted Grades Above 90: ",high_grades)
