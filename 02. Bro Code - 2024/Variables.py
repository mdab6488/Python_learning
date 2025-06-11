# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# String
print("*" * 30)
print("STRING")
print("*" * 30)
first_name = "MD"
last_name = "ABDUR RAHMAN"
food = "Biryani"
email = "mdab6488@gmail.com"

# print(first_name + " " + last_name)
print(f"MY NAME IS: {first_name} {last_name}")
print(f"I like {food}")
print(f"Your email is: {email}")

# Integers
print("*" * 30)
print("INTEGERS")
print("*" * 30)
age = 27
quantity = 3
num_of_students = 30

print(f"I am {age} years old")
print(f"I am buying {quantity} items")
print(f"My class has {num_of_students} students")

# Float
print("*" * 30)
print("FLOAT")
print("*" * 30)

price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is {price}")
print(f"My gpa is: {gpa}")
print(f"I run {distance}km")

# Boolean
print("*" * 30)
print("BOOLEAN")
print("*" * 30)

is_student = False
for_sale = True
is_online = True

if is_student:
    print("I am a student")
else:
    print("I am not an student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT avaiable")

if is_online:
    print("You are online")
else:
    print("You are offline")