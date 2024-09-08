#Exercise 2: Student Enrollment

#Requirements:

    #Create a Student class with instance variables name and grade.
    #Add a class variable school_name representing the name of the school.
    #Add a class variable student_count to keep track of how many students have been enrolled.
    #Create a method that prints the total number of students enrolled and the school name.
class Student:
    school_name = "International Melbourne"
    student_count = 0
    def __init__(self, name, grade, sex):
        self.name = name
        self.grade = grade
        self.sex = sex
        Student.student_count += 1
    def stu_info(self):
        print(f"Student information: {self.name}, grade {self.grade}, {self.sex}")

stu1 = Student("Peter Parker", 12, "Male")
stu2 = Student("Anna Taylor-Joy", 10, "Female")
stu3 = Student("David Beckham", 11, "Male")


print("School's Name:", Student.school_name)
print("Total number of student:", Student.student_count)
stu1.stu_info()
stu2.stu_info()
stu3.stu_info()


#update class variable 
#update object 


school_name = "International Melbourne"
stu1 = Student("Peter Parker", 12, "Male")
Student.school_name = "High school"
stu1.name = "Alan 





































    






















