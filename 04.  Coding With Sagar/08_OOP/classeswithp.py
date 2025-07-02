# polymorphism with classes
class Brid:
    def sound(self):
        print("Birds make sounds")

class Crow(Brid):
    def sound(self):
        print("Cow say 'Caw Caw'")

class Parrot(Brid):
    def sound(self):
        print("Parrot sounds 'squawk'")

bird1 = Crow()
bird2 = Parrot()

bird1.sound() # Cow say 'Caw Caw'
bird2.sound() # Parrot sounds 'squawk'

print(bird1) # <__main__.Crow object at 0x000001519DB06F90>
print(bird2) # <__main__.Parrot object at 0x000001519DB070E0>
