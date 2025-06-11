marks = {
    "Riyan": 100,
    "Alamin": 56,
    "MD AB": 23,
    0: "Riyan Kabir"
}

print()
# print(marks.items()) # dict_items([('Riyan', 100), ('Alamin', 56), ('MD AB', 23), (0, 'Riyan Kabir')])

for i in marks.keys():
    print(i)
print()
for i in marks.values():
    print(i)
marks.update({"Alamin": 50, "new_item": 99})
print()
for i in marks.items():
    print(i)
print()
print(marks.get("Alamin")) # 50
print(marks["Alamin"]) # 50
print()
print(marks.get("Alamin2")) # None
# print(marks["Alamin2"]) # KeyError: 'Alamin2'