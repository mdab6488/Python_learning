students = [
    {"name": "Riyan", "house": "Uttara Sector 3"},
    {"name": "Alamin", "house": "Matikata"},
    {"name": "MD AB", "house": "Matikata"},
    {"name": "Riyan Kabir", "house": "Uttara Sector 3"},
    {"name": "MD Abdur Rahman", "house": "Matikata"},
    {"name": "Alamin + Riyan", "house": "Canada"}
]

print()
# print(type(students)) # <class 'list'>
# print(type(students[1])) # <class 'dict'>

# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])
#
# for house in sorted(houses):
#     print(house)

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)