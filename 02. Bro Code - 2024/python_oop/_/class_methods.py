# Class methods = Allow operations related to class itself
#                 Take (cls) as the first parameter

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility fuctions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself


class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # CLASS METHOD
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"


student1 = Student(name="Riyan", gpa=5.0)
student2 = Student(name="Alamin", gpa=4.0)
student3 = Student(name="MD Abdur Rahman", gpa=3.12)

print("*" * 30)
print(Student.get_count())
print(Student.get_average_gpa())
print("*" * 30)


