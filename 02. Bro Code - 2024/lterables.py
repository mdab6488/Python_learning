# lterables = An object/collecion that can return its elements one at a time, allowing it to be iterated over in a loop

print(f"{"*" * 24}")
print(f"{" " * 8} LIST {" " * 8}")
print(f"{"*" * 24}")
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number, end=" ")

print()

for number in reversed(numbers):
    print(number, end=" ")

print("\n")
print(f"{"*" * 24}")
print(f"{" " * 8} TUPLE {" " * 8}")
print(f"{"*" * 24}")
numbers2 = (1, 2, 3, 4, 5)

for number in numbers2:
    print(number, end=" ")

print()

for number in reversed(numbers2):
    print(number, end=" ")

print("\n")
print(f"{"*" * 24}")
print(f"{" " * 8} SETS {" " * 8}")
print(f"{"*" * 24}")

fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit, end=" ")

print()

# TypeError: 'set' object is not reversible
# for fruit in reversed(fruits):
#     print(fruit, end=" ")

print("\n")
print(f"{"*" * 24}")
print(f"{" " * 8} STRINGS {" " * 8}")
print(f"{"*" * 24}")
name = "MD ABDUR RAHMAN"

for x in name:
    print(x, end="-")

print()

for x in reversed(name):
    print(x, end="-")

print("\n")
print(f"{"*" * 24}")
print(f"{" " * 6} DICTIONARY {" " * 6}")
print(f"{"*" * 24}")

my_dictionary = {"A": 1,
                 "B": 2,
                 "C": 3}
for key in my_dictionary:
    print(key, end=" ")

print()

for key in reversed(my_dictionary):
    print(key, end=" ")

print("\n")

for value in my_dictionary.values():
    print(value, end=" ")

print()

for value in reversed(my_dictionary.values()):
    print(value, end=" ")

print("\n")

for key, value in my_dictionary.items():
    print(f"{key:3}: {value}")

print()

for key, value in reversed(my_dictionary.items()):
    print(f"{key:3}: {value}")