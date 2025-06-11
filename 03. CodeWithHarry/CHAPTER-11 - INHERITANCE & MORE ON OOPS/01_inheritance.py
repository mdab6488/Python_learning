class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infortech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
#
#     def show_language(self):
#         print(f"The name is {self.name} and he is goo {self.language} language")

class Programmer(Employee):
    company = "ITC Infortech"
    def show_language(self):
            print(f"The name is {self.name} and he is good at {self.language} language")

a = Employee()
b = Programmer()

print()
print(a.company, b.company)