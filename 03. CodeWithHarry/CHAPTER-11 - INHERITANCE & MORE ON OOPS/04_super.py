class Employee:
    def __init__(self):
        print("Constructor of Employee")

    a = 1


class Programmer(Employee):
    # def __init__(self):
    #     print("Constructor of Programmer")
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    b = 2


class Manager(Programmer):
    # def __init__(self):
    #     print("Constructor of Manager")
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3


print()
o = Employee()
print(o.a)  # Prints the attribute

print()
o = Programmer()
print(o.a, o.b)

print()
o = Manager()
print(o.a, o.b, o.c)