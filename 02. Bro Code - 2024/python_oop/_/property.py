# @property = Decorator used to define a method as a property (it can be accessed like and attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method

class Reactangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    # getter
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # setter
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greather then zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greather then zero")

    # deleter
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Reactangle(width=3, height=4)

# print(rectangle._width) # 3 # Access to a protected member _width of a class
# print(rectangle._height) # 4 # Access to a protected member _height of a class
print()

print(rectangle.width) # 3.0cm
print(rectangle.height) # 4.0cm
print()

rectangle.width = 5
rectangle.height = 7

print(rectangle.width)
print(rectangle.height)
print()

del rectangle.width
del rectangle.height
