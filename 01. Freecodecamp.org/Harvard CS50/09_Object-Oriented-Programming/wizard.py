# docs.python.org/3/libray/exceptions.html
"""
BaseException
    KeyboardInterrupt
    Exception
        ArithmeticError
            ZeroDivisionError
        AsseributeError
        AttributeError
        EOFError
        ImportError
            ModuleNotFoundError
        LookupError
            KeyError
        NameError
        SyntaxError
            IndentationError
        ValueError
"""
print()

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self, name, house):
        # if not name:
        #     raise ValueError("Missing Name")
        # self.name = name
        super().__init__(name)
        self.house = house

    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        # if not name:
        #     raise ValueError("Missing Name")
        # self.name = name
        super().__init__(name)
        self.subject = subject

    ...

wizard = Wizard("Abroad")
student = Student("Riyan", "Uttra")
professor = Professor("Alamin", "I am nice Top")

