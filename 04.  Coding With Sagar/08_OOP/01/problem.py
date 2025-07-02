print()
class Car:

    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

        print(brand, color)

car1 = Car()
car1.set_details("Tesla", "Red")

