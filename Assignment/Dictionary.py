courses = {
    "CSE101" : {
        "Course name" : "Introduction to Programming",
        "Credits" : 3,
        "Instructor" : "Dr. Alice"
    },
    "CSE102" : {
        "Course name" : "DataStructure",
        "Credits" : 4,
        "Instructor" : "Dr. Bob"
    },
    "CSE103" : {
        "Course name" : "Daatabaase System",
        "Credits" : 3,
        "Instructor" : "Dr. Carol"
    }
}
print("The Dictionary:\n",courses)
print("\n")

#Update the instructor's name
x = courses["CSE102"]["Istructor"] = ["Dr. Bob Jr"]
print("Update the Instructor name:",x)
print("\n")



#Add a new course
courses["CSE104"] = {
    "Course name" : "Algorithms",
    "Credits" : 4,
    "Instructor" : "Dr. Dave"  
}
print("Add the course:\n",courses)
print("\n")


#Remove the course
courses.pop("CSE101")
print("After removing the course:\n",courses)
print("\n")


#Loop through the dictionary
print("Printing course details:")
for course_code, course_details in courses.items():
    print(f"Course Code: {course_code}")
    for detail, value in course_details.items():
        print(f"  {detail}: {value}")