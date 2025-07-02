class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("BMW", "RED") # Values automatically set
print(car1) # <__main__.Car object at 0x000001E4D9F16F90>
print(car1.brand, car1.color) # BMW RED

"""
syntax:
class ClassName:
    def __init__(self, parameters1, parameters2)
        self.parameters1 = parameter1
        self.parameters2 = parameters2

__init__() constructor
self.property:
"""