# ====================================
# Variables
# ====================================
# sourcery skip: merge-assign-and-aug-assign

# name = "Riyan"
# age = 23
# is_student = True

# ====================================
# Expressions & Statements
# ====================================
# name = "Riyan"
# print(name)

# ====================================
# Data Types
# ====================================
# str_type = "Hello World"
# int_type = 42
# float_type = 3.14
# bool_type = True
# list_type = [1, 2, 3, 4, 5]
# tuple_type = (1, 2, 3, 4, 5)
# dict_type = {"name": "Riyan", "age": 23}
# set_type = {1, 2, 3, 4, 5}
# None_type = None

# number = "100"
# sting_to_int = int(number)


# print(type(sting_to_int))
# print(isinstance(sting_to_int, int))

# complex for complex numbers
# bool for booleans
# list for lists
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets

# ====================================
# Number data type
# ====================================
num1 = 2 + 3j  # complex number
num2 = complex(2, 3)
print(num2.real, num2.imag)
# ====================================
# Operators
# ====================================
# age = 20  # Assignment operator

# --------------------
# Arithmetic operator
# --------------------
# 1 + 1  # 2
# 1 + -1  # 0
# 2 - 1  # 1
# 2 * 2  # 4
# 4 / 2  # 2.0
# 4 % 3  # 1
# 4**2  # 16
# 5 // 2  # 2

# print("Scamp" + " is a good dog")

# age = 8
# age += 9  # age = age + 9
# print(age)  # 16

# --------------------
# Comparison operator
# --------------------
# a = 1
# b = 2

# a == b  # False
# a != b  # True
# a > b  # False
# a < b  # True
# a >= b  # False
# a <= b  # True

# --------------------
# Boolean operator
# --------------------
# condition1 = True
# condition2 = False

# not condition1  # False
# condition1 and condition2  # False
# condition1 or condition2  # True

# print(0 or 1)  # 1
# print(False or "Hey")  # 'Hey'
# print("Hi" or "Hey")  # 'Hi'
# print([] or False)  # False
# print(False or [])  # []

# print(0 and 1)  # 0
# print(1 and 0)  # 0
# print(False and "Hey")  # False
# print("Hi" and "Hey")  # 'Hey'
# print([] and False)  # []
# print(False and [])  # False

# done = True
# print(type(done) == bool)  # True

# if done:
#     print("Done")
# else:
#     print("Not Done")

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
print(read_any_book)  # True


read_any_book = all([book_1_read, book_2_read])
print(read_any_book)  # False
# --------------------
# Bitwise operator
# --------------------
# & performs binary AND
# | performs binary OR
# ^ performs binary XOR operation
# ~ performs binary NOT operation
# << performs left shift operation
# >> performs right shift operation

# --------------------
# is & in operator
# --------------------
# is a = 1 is 1  # True
# is b = 1 is not 2  # True
# is c = 1 in [1, 2, 3]  # True
# is d = 1 not in [2, 3, 4]  # True

# in [1, 2, 3]  # True
# is [1, 2, 3] in [1, 2, 3]  # True
# is [1, 2, 3] not in [1, 2, 3]  # False
# is [1, 2, 3] is [1, 2, 3]  # True
# is [1, 2, 3] is not [1, 2, 3]  # False


# --------------------
# Ternary operator
# --------------------
# def is_adult(age):
#     # sourcery skip: assign-if-exp, boolean-if-exp-identity, remove-unnecessary-cast
#     if age >= 18:
#         return True
#     else:
#         return False


# def is_adult2(age):
#     # sourcery skip: boolean-if-exp-identity, remove-unnecessary-cast
#     return True if age >= 18 else False


# ====================================
# Strings
# ====================================
# "Riyan love me"
# "I love Riyan"

# name = "Alamin"
# lover = "Riyan"
# phrase = "I love Riyan" + " " + "very much"
# name += f" love {lover} very much"
# age = str(23)
# print(name)

# print(
#     f"""Riyan is

# {age}

# Years old.
# """
# )

# ====================================
# String Methods
# ====================================
# names = "Riyan, alamin"
# print(names.lower())  # riyan, alamin
# print(names.upper())  # RIYAN, ALAMIN
# print(names.title())  # Riyan, Alamin
# print(names.capitalize())  # Riyan, alamin
# print(names.strip())  # Riyan, alamin
# print(names.lstrip())  # Riyan, alamin
# print(names.rstrip())  # Riyan, alamin
# print(names.replace("a", "A"))  # RiyAn, AlAmin
# print(names.split("a"))  # ['Riy', 'n, ', 'l', 'min']
# print(names.split())  # ['Riyan,', 'alamin']
# print(names.split(" "))  # ['Riyan,', 'alamin']
# print(names.splitlines())  # ['Riyan, alamin']
# print(names.find("a"))  # 2
# print(names.index("a"))  # 2
# print(names.count("a"))  # 2

# print("an" in names)  # True
# print("an" not in names)  # False


# print(len(names))  # 13


# ---------------------------------------------------
# isalpha()  # to check if a string contains only characters and is not empty
# isalnum()  # to check if a string contains characters or digits and is not empty
# isdecimal()  # to check if a string contains digits and is not empty
# lower()  # to get a lowercase version of a string
# islower()  # to get a lowercase version of a string
# upper()  # to get a uppercase version of a string
# isupper()  # to get a uppercase version of a string
# title()  # to get a capitalized version of a string
# startsswith()  # to check if a string starts with a specific character
# endswith()  # to check if a string ends with a specific character
# replace()  # to replace a specific character in a string with another character
# split()  # to split a string into a list of strings based on a specific character
# strip()  # to remove leading and trailing whitespace from a string
# join()  # to join a list of strings into a single string with a specific character
# find()  # to find the index of a specific character in a string

# ====================================
# Escaping Characters
# ====================================
# escaped_string = 'I love \nRiyan "very much"'
# print(escaped_string)  # I love
# # Riyan "very much"

# ====================================
# String Characters & Slicing
# ====================================
# name = "Riyan Kabir"
# print(name[0])  # R
# print(name[1])  # i
# print(name[2])  # y
# print(name[3])  # a
# print(name[4])  # n
# print(name[1:2])  # i
# print(name[1:3])  # iy
# print(name[2:])  # yan Kabir
