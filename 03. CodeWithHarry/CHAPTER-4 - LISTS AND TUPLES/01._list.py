items = ["Apple", "Orange", 5, 345.06, False, "Riyan", "Alamin"]

print()
print(type(items)) # <class 'list'>
print(items[0])
print()
print(items[1:4])
print()
items[0] = "Grapes" # Unlike Strings lists are mutable
print()

for item in items:
    print(item)
