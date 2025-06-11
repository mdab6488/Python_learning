# multiple inheritance = an inherit form more than one parent class
#                        C(A, B)
# multelevel inheritance = inherit from a parent which inherits another parent
#                        C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): #
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
rabbit.sleep()
rabbit.flee()
# rabbit.hunt() # 'Rabbit' object has no attribute 'hunt'
print()
hawk.eat()
hawk.sleep()
hawk.hunt()
# hawk.flee() # 'Hawk' object has no attribute 'flee'
print()
fish.eat()
fish.sleep()
fish.flee()
fish.hunt()