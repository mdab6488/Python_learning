print()

"""
__init__()

"""

class Car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car()
car1.set_details("Tesla", "Red")

print(car1.brand)
print(car1.color)