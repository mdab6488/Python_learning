"""Dog module

This moule does ... bla bla bla and provides the following classes:

- Dog
...
"""

# def increment(n):
#     """Increment the given number by 1."""
#     return n + 1


class Dog:
    """A class representing a dog."""

    def __init__(self, name, age):
        """Initialize the dog with a name and age."""
        self.name = name
        self.age = age

    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says Woof!"


print(help(Dog))  # Show the docstring of the Dog class
