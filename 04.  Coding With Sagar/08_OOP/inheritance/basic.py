class Animal:
    def speak(self):
        print("Animal make sounds")

class Dog(Animal):
    def bark(self):
        print("Dogs Bark")

dog = Dog()
dog.speak() # Animal make sounds
dog.bark() # Dogs Bark
