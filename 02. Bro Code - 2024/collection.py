from pprint import pprint
# Collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchngeable. Duplicates OK. FASTER

print("*" * 30)
print("List = []")
print("*" * 30)
# fruit = "apple"
# print(fruit)

fruits = ["apple", "orange", "mango", "banana"]
# print(fruits[0])
# print(fruits[1].capitalize())
# print(fruits[2].upper())
# print(fruits[3])
#
# print()
# print(fruits[:3])
# print(fruits[::2])
# print(fruits[::-1])
#
# for fruit in fruits:
#     print(fruit)

# pprint(dir(fruits))
# print(help(fruits))

# print(len(fruits))

# print("pineapple" in fruits)

# fruits[1] = "pineapple"
# for fruit in fruits:
#     print(fruit)

# fruits.append("pineapple")
# fruits.remove("banana")
# fruits.insert(0, "pineapple")

# fruits.sort()
# fruits.reverse()
#
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))
#
print(fruits)

print("*" * 30)
print("Set = {}")
print("*" * 30)
fruits = {"apple", "orange", "banana", "coconut", "coconut"}

# pprint(dir(fruits))
# print("pineapple" in fruits)
# print(fruits[0]) ❌
# fruits.add("pineapple")
# fruits.remove("pineapple")
# fruits.pop() # Randomly delete 1 item
# fruits.clear()

print(fruits)

print("*" * 30)
print("Tuple = ()")
print("*" * 30)

fruits = ("apple", "orange", "banana", "coconut", "coconut")

# pprint(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)
# print(fruits.index("apple"))
# print(fruits.count("banana"))

print(fruits)

for fruit in fruits:
    print(fruit)