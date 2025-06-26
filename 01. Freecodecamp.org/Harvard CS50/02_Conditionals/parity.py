# +                 # Addition
# -                 # Subtraction
# *                 # Multiplication
# /                 # Division
# %                 # Modulo Operator
print()

# x = int(input("What's x? "))
#
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

def main():
    x = int(input("What's x? "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(number):
    # if number % 2 == 0:
    #     return True
    # return False

    # return True if number % 2 == 0 else False

    return number % 2 == 0

main()

