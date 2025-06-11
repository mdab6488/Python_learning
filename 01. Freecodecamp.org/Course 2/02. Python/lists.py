from pprint import pprint

# list = ["Riyan", 1, "Alamin", True, "anything", 1.5]
# list[2] = ["Riyan Love me", "Alamin Love Riyan"]

# # print("Riyan" in list)  # True
# # print(list[2])  # Alamin
# # print(list)  # ["Riyan", 1, ['Riyan Love me', 'Alamin Love Riyan'], True]
# # print(list[2][1])  # Alamin Love Riyan
# # print(list[-1])  # True
# # print(list[2:4])  # [['Riyan Love me', 'Alamin Love Riyan'], True]
# # print(list[3:])  # [True]

# list.append("Riyan 🥰 Alamin")
# list.extend(["anything2", 2.5])

# list += ["anything3", 3.5]

# list.remove("anything")

# # print(len(list))

# print(list.pop())

# pprint(
#     list
# )  # ["Riyan", 1, ['Riyan Love me', 'Alamin Love Riyan'], True, "Riyan 🥰 Alamin"]

# items = ["Riyan", 1, "Alamin", True, "anything", 1.5]

# items.insert(0, "Riyan Love me")
# pprint(items)  # ['Riyan Love me', 'Riyan', 1, 'Alamin', True, 'anything', 1.5]
# items.insert(
#     2, "Alamin Love Riyan"
# )  # ['Riyan Love me', 'Riyan', 'Alamin Love Riyan', 1, 'Alamin', True, 'anything', 1.5]
# pprint(items)

# items[1:1] = ["Test1", "Test2"]
# pprint(items)

# =================================
# Sorting Lists
# =================================
sort_items = ["Riyan", "Alamin", "Love"]

# itemscopy = sort_items[:]

# sort_items.sort(key=str.lower)
# pprint(sort_items)  # ['Alamin', 'Love', 'Riyan']

# sort_items.sort(reverse=True)
# pprint(sort_items)  # ['Riyan', 'Love', 'Alamin']
# print("")
# pprint(
#     itemscopy
# )  # ['Riyan Love me', 'Riyan', 'Alamin Love Riyan', 1, 'Alamin', True, 'anything', 1.5]


pprint(sorted(sort_items, key=str.lower))  # ['Alamin', 'Love', 'Riyan']
print("")
pprint(sort_items)  # ['Riyan', 'Alamin', 'Love']
