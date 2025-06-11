class Employee:
    a = 1


class Programmer(Employee):
    b = 2


class Manager(Programmer):
    c = 3


print()
o = Employee()
print(o.a)  # Prints the attribute
# print(o.b) # Show an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)