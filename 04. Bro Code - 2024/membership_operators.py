# membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set or dictonary)
#                        1. in
#                        2. not in

print(f"{"*" * 24}")
print(f"{" " * 8} STRINGS {" " * 8}")
print(f"{"*" * 24}")
word = "APPLE"
print(word)
# letter = input("Guess a letter in the secret word: ")
#
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")
#
# print("-" * 20)
#
# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")

email = input("Enter your email address: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")

print(f"{"*" * 24}")
print(f"{" " * 2} LIST, TUPLE, SET {" " * 2}")
print(f"{"*" * 24}")
students = {"Riyan",
            "Alamin",
            "Abdur Rahman"}
print(students)
# student = input("Enter the name of a studeny: ")
#
# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")
#
# print("-" * 30)
#
# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a student")

print(f"{"*" * 24}")
print(f"{" " * 8} DICTIONARY {" " * 8}")
print(f"{"*" * 24}")
grades = {"Riyan": "A",
          "Alamin": "B",
          "Abdur Rahman": "C"}
print(grades)
# student = input("Enter the name of a studeny: ")
#
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")
#
# print("-" * 30)
#
# if student not in grades:
#     print(f"{student} was not found")
# else:
#     print(f"{student}'s grade is {grades[student]}")