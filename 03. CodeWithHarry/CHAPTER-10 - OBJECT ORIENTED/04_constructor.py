print()
class Employee:
    language = "English" # This is a class attribute
    salary = 1200000 # This is a class attribute

    def __init__(self, name, language, salary): # dunder method which is automatically called
        self.name = name
        self.language = language
        self.salary = salary

    def get_info(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

employee1 = Employee(name="Riyan", language="Javascript", salary=1200000)
print(employee1.name, employee1.language, employee1.salary)

print()
employee2 = Employee(name="MD AB", language="Python", salary=1000000)
print(employee2.name, employee2.language, employee2.salary)





