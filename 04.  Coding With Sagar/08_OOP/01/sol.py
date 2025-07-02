print()

class Student:
    def set_details(self, name, age):
        self.name = name
        self.age = age

student1 = Student()
student1.set_details("Alamin", 90)
print(student1.name, student1.age)


