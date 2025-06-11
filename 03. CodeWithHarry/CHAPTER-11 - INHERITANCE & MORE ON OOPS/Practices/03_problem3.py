class Employee:
    salary = 234
    increment = 20

    @property
    def salary_after_increment(self):
        return self.salary + self.salary * (self.increment/100)

    @salary_after_increment.setter
    def salary_after_increment(self, salary):
        self.increment = ((salary/self.salary) - 1) * 100

print()
e = Employee()
# print(e.salary_after_increment)
e.salary_after_increment = 280
print(e.increment)

