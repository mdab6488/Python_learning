# if __name__ == __main__: (this script can be imported OR run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular,
#                helps readability,
#                leaves no global variables,
#                avoid unintended execution)

#               Ex. Library = import library for functionality
#                   When running library directly, display a help page


# print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# print(__name__) # __main__

# if __name__ == '__main__':
#     main()

# from script2 import *
# print(__name__) # __main__

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print(f"This is {__name__}")

    favorite_food("Pizza")
    print("Goodbye!")

if __name__ == '__main__':
    main()
