class Employee:
    a = 1

    def __init__(self):
        self.fname = None
        self.lname = None

    @classmethod
    def show(cls):
        print(f"The classe attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

print()
e = Employee()
e.a = 45

e.name = "Riyan Kabir"
print(e.fname, e.lname)

e.show()