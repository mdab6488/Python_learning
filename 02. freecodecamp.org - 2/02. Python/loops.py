# condition = True
# while condition:
#     print("Hello World")
#     condition = False  # This will stop the loop after one iteration

# count = 0

# while count < 10:
#     print("The condtion is True")
#     count += 1  # Increment the count by 1 each time the loop runs

# print("Loop finished")

# items = ["apple", "banana", "cherry"]
# for item in items:
#     print(item)

# for item in range(23):
#     print(item)

# items = ["apple", "banana", "cherry"]
# for index, item in enumerate(items):
#     print(f"{index}. {item}")

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for item in items:
#     if item == 5:
#         continue
#     print(item)

for item in items:
    if item == 5:
        break
    print(item)
