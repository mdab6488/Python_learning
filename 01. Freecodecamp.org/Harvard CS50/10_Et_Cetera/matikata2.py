# dictionary comprehension

print()
# students = ["Alamin", "Riyan", "MD Abdur Rahman"]
#
# matikata = []
#
# for student in students:
#     matikata.append({
#         "name": student,
#         "house": "Matikata"
#     })
#
# print(matikata)
# # [{'name': 'Alamin', 'house': 'Matikata'}, {'name': 'Riyan', 'house': 'Matikata'}, {'name': 'MD Abdur Rahman', 'house': 'Matikata'}]

# students = ["Alamin", "Riyan", "MD Abdur Rahman"]
#
# matikata = [{"name": student, "house": "Matikata"} for student in students]
#
# print(matikata)
# # [{'name': 'Alamin', 'house': 'Matikata'}, {'name': 'Riyan', 'house': 'Matikata'}, {'name': 'MD Abdur Rahman', 'house': 'Matikata'}]

students = ["Alamin", "Riyan", "MD Abdur Rahman"]

matikata = {student: "Matikata" for student in students}

print(matikata)
# {'Alamin': 'Matikata', 'Riyan': 'Matikata', 'MD Abdur Rahman': 'Matikata'}


