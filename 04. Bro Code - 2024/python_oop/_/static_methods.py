# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usally used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

# INSTANCE METHOD
# def get_info(self):
#     return f"{self.name} = {self.position}"

# STATICMETHOD METHOD
# @staticmethod
# def km_to_miles(kilometers):
#     return kilometers * 0.621371

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee(name="MD AB", position="Cook")
employee2 = Employee(name="Riyan", position="Cashier")
employee3 = Employee(name="Alamin", position="Janitor")
employee4 = Employee(name="Riyan Kabir", position="manager")

# employee1 = Employee()
print(Employee.is_valid_position("Cook"))
print()
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())