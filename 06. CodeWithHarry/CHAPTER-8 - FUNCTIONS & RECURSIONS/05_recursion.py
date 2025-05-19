"""
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)
"""
from math import factorial

print()
def function(number):
    if number==1 or number==0:
        return 1
    return number * factorial(number - 1)

n = int(input("Enter you number: "))
print(f"The factorial of this number is: {factorial(n)}")

"""
Factorial(5)
5XFactorial(4)
5x4x3xFactorial(2)
5X4X3X2XFactorial(1)
5X4X3X2X1
"""