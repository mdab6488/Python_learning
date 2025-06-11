class Employee:
    company = "ITC"
    name = "Default Name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def print_languages(self):
        print(f"Out of all the languages here is your langugage: {self.language}")

class Programmer(Employee, Coder):
    company = "ITC Infortech"
    def show_language(self):
            print(f"The name is {self.company} and he is good at {self.language} language")

a = Employee()
b = Programmer()

print()
# print(a.company, b.company)
b.show()
b.print_languages()
b.show_language()
