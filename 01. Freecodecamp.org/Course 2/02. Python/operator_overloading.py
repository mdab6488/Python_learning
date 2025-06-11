class Dog:
    # The Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        # Overloading the greater than operator
        return self.age > other.age


roger = Dog("Roger", 5)
syd = Dog("Syd", 7)

print(roger > syd)  # False

# __add__() respond to the + operator
# __sub__() respond to the - operator
# __mul__() respond to the * operator
# __truediv__() respond to the / operator
# __floordiv__() respond to the // operator
# __mod__() respond to the % operator
# __pow__() respond to the ** operator
# __rshift__() respond to the >> operator
# __lshift__() respond to the << operator
# __and__() respond to the & operator
# __or__() respond to the | operator
# __xor__() respond to the ^ operator
