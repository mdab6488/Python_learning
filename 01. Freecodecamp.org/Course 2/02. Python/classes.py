class Animal:
    def walk(self):
        print("Walking...")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof! Woof!")


doggy = Dog("Roger", 5)

# print(type(doggy))  # Output: <class '__main__.Dog'>
print(
    f"Dog's name: {doggy.name} & age: {doggy.age}"
)  # Output: Dog's name: Roger & age: 5
doggy.bark()  # Output: Woof! Woof!
doggy.walk()  # Output: Walking...
