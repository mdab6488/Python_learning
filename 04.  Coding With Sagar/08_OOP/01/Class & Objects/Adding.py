print()
class Car:
    def __init__(self):
        self.brand = None
        self.color = None

    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

    def show_details(self):
        print(f"This car is a {self.color} {self.brand}")

car1 = Car()
car1.set_details("Tesla", "Red")
car1.show_details()

car2 = Car()
car2.set_details("BMW", "Blue")
car2.show_details()

