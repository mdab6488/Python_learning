class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The classe attribute of a is {cls.a}")

print()
e = Employee()
e.a = 45

e.show()