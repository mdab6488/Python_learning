print()
try:
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 1: "))
    try:
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("You cannot divide with zero")
except ValueError:
    print("You must provide a valid input")

