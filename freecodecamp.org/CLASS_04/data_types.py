import math

# String data type


first = "Abdur"
last = "Rahman"

# print(type(first))
# # print(type(first) == str)
# print(isinstance(first, str))

# Constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# # print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
# fullname = first + " " + last
fullname = f"{first} {last}"
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)


# statement = "I like rock music from the " + decade + "s."
statement = f"I like rock music from the {decade}s."
print(statement)

# Muliple Lines
multiline = """
Hey, how are you?

I was just checking in. 
                        All good?
"""
print(multiline)

# Escaping speacial Characters
sentence = "I'm back at work!\tHey!\n\nWhere's this at\\located?"
print(sentence)

# String Methods
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                  "
# multiline = "                                      " + multiline
multiline = f"                                      {multiline}"
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")


# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffe".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# String Index Values
print(first[0])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("A"))
print(first.endswith("R"))

# Boolean data type
myvalue = True
# x = bool(False)
x = False
print(type(x))
print(isinstance(x, bool))

# Numaric data types
## Integer
price = 100
# best_price = int(80)
best_price = 80
print(type(price))
print(isinstance(price, int))

## float type
gpa = 3.28
# y = float(1.14)
y = 1.14
print(type(gpa))

# complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")
