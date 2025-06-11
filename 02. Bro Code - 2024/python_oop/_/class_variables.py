# class variables = shared among all instances of class
#                   Defined outside the constructor
#                   Allow you to share data among all objects create from that class

class Student:

    class_year = 2026
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1


student1 = Student("Riyan", 23)
student2 = Student("Alamin", 27)
student3 = Student("MD AB", 28)

print("*" * 30)
print(f"My graduating class of {Student.class_year} has {Student.num_student} students")
print("*" * 30)
print(f"I am {student1.name} & my age {student1.age} years old.")
print(f"I am {student2.name} & my age {student2.age} years old.")
print(f"I am {student3.name} & my age {student3.age} years old.")


