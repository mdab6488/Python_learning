"""
if condition:
    statements
elif condition:
    statements
else:
    statements
"""
print()
age = int(input("Enter your age = "))

if 18 <= age <= 100 :
    print("You can vote!")
elif age < 0 or age > 100:
    print("Invalid Age")
else:
    print("You are less then 18 years old")
