# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

# class Father:
#     height = 182
#     color = "pink"
#
# class Son(Father):
#     pass

# Animal
#   Dog
#   Cat
#   Mouse

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()
print()
print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()
print()
print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
cat.speak()