# Python Calculator

operator = input("Enter and operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the 2nd number: "))

# print(num1 + num2)
if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not valid operator")