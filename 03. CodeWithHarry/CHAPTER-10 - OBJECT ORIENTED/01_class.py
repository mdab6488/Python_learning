print()
class Employee:
    language = "English" # This is a class attribute
    salary = 1200000 # This is a class attribute

employee1 = Employee()
employee1.name = "Riyan" # This is an instance attribute
print(employee1.name ,employee1.language, employee1.salary)

employee2 = Employee()
employee2.name = "MD AB" # This is an instance attribute
print(employee2.name ,employee2.language, employee2.salary)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class




