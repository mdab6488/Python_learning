# object = A "bundle" of related attributes (varuables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("Mustang", "2025", "red", False)
car2 = Car("Corvette", "2020", "blue", True)
car3 = Car("Charger", "2026", "yellow", True)

# print(car1) # <__main__.Car object at 0x0000028ACAD06900>
# print(car1.model) # Mustang
# print(car1.year) # 2025
# print(car1.color) # red
# print(car1.for_sale) # False
# print()
# print(car2.model) # Mustang
# print(car2.year) # 2025
# print(car2.color) # red
# print(car2.for_sale) # False
# print()
# print(car3.model) # Mustang
# print(car3.year) # 2025
# print(car3.color) # red
# print(car3.for_sale) # False

car1.drive()
car2.drive()
car3.drive()
print()
car1.stop()
car2.stop()
car3.stop()
print()
car1.describe()
car2.describe()
car3.describe()