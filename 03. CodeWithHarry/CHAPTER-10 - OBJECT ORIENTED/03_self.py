print()
class Employee:
    language = "English" # This is a class attribute
    salary = 1200000 # This is a class attribute

    def get_info(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

employee1 = Employee()
employee1.greet()
employee1.get_info()
# Employee.get_info(employee1)

print()
employee2 = Employee()
employee2.language = "Python" # This is an instance attribute
employee2.greet()
employee2.get_info()
# Employee.get_info(employee2)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class




