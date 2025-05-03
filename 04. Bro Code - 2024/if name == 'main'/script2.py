from script1 import *

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print(f"This is {__name__}")
    favorite_food("Briany")
    favorite_drink("coffee")
    print("Goodbye!")

if __name__ == '__main__':
    main()