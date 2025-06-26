print()
# def main():
#     name = input("What's your name? ")
#     hello(name)
#
# def hello(to="Alamin"):
#     print(f"hello, {to}")
#
# main()

def main():
    x = int(input("What's x? "))
    # y = int(input("What's y? "))

    print(f"x squared is {square(x)}")

def square(number):
    return number * number

main()