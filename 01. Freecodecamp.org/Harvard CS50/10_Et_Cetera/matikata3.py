# docs.python.org/3/library/functions.html#enumerate


print()

students = ["Alamin", "Riyan", "MD Abdur Rahman"]

# for student in students:
#     print(f"{student}")
# # Alamin
# # Riyan
# # MD Abdur Rahman

# for i in range(len(students)):
#     print(f"{i + 1}. {students[i]}")
# # 1. Alamin
# # 2. Riyan
# # 3. MD Abdur Rahman

for key, value in enumerate(students, start=1):
    print(f"{key}. {value}")
# # 1. Alamin
# # 2. Riyan
# # 3. MD Abdur Rahman