# list comprehensions
# pip install black
# black matikata.py

print()
students = [
    {"name": "Riyan", "house": "Uttara Sector 3"},
    {"name": "Alamin", "house": "Matikata"},
    {"name": "MD AB", "house": "Matikata"},
    {"name": "Riyan Kabir", "house": "Uttara Sector 3"},
    {"name": "MD Abdur Rahman", "house": "Matikata"},
    {"name": "Alamin + Riyan", "house": "Canada"},
]

# form_matikata = [
#     student["name"] for student in students if student["house"] == "Matikata"
# ]
#
# for student in sorted(form_matikata):
#     print(student)

# def is_matikata(s):
#     return s["house"] == "Matikata"

# form_matikata = filter(is_matikata, students)
form_matikata = filter(lambda s: s["house"] == "Matikata", students)

for student in sorted(form_matikata, key=lambda s: s["name"]):
    print(student["name"])
