# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print(f"Value is equal to {value}")

# names = ["John", "Jane", "Doe"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Jane":
#         break
#     print(x)

# for x in names:
#     if x == "Jane":
#         continue
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(2, 4):
#     print(x)


# for x in range(5, 101, 5):
#     print(x)
# else:
#     print("Loop finished")

# for x in range(5, 101, 5):
#     print(x)

# print("Loop finished")

names = ["John", "Jane", "Doe"]
actions = ["eat", "sleep", "code"]

# for name in names:
#     for action in actions:
#         print(f"{name} likes to {action}")

# from itertools import product

# for name, action in product(names, actions):
#     print(f"{name} likes to {action}")

for action in actions:
    for name in names:
        print(f"{name} likes to {action}")
