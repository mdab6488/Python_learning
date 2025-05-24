# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
#
# age += 1
#
# print("-" * 30)
# print(f"Hello, {name}!")
# print("Happy Birthday!")
# print(f"I am {age} years old.")

# ========================================
# Exercise 1 Rectangle Area Calc
# ========================================
# length = float(input("Enter the length(cm): "))
# width = float(input("Enter the width(cm): "))
#
# area = length * width
#
# print(f"The area is: {area}cm^2")

# ========================================
# Exercise 2 Shopping Cart Program
# ========================================
item = input("What item whould you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print("*" * 50)
print(f"You have bought {quantity} x {item}")
print(f"Total ammount you need to pay: ${total}")
print("*" * 50)








