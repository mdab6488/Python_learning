print()

# l = [0, 2, 4, 8, 3, 5]
#
# for i in l:
#     print(i)
#
# for i in [0, 1, 2]:
#     print("meow")
#
# print()
#
# for _ in range(3):
#     print("bak bak")

# students = ["Alamin", "Riyan Kabir", "MD Abdur Rahman"]
# locations = ["ECB", "Uttara", "ECB"]
#
# # print(students[0])
# # print(students[1])
# # print(students[2])
# # for student in students:
# #     print(student)
#
# for i in range(len(students)):
#     # print(i + 1, students[i])
#     print(f"{i + 1}. {students[i]}")
#
# print()
# infos = {
#     "Alamin": "ECB",
#     "Riyan Kabir": "Uttara",
#     "MD Abdur Rahman": "ECB"
# }
# print(type(infos))
#
# # print(infos["Alamin"])
# # print(infos["Riyan Kabir"])
# # print(infos["MD Abdur Rahman"])
#
# for info in infos:
#     print(f"{info} live in {infos[info]}")

students = [
    {
        "name": "Alamin",
        "house": "ECB",
        "study": "Web Development"
    },
    {
        "name": "Riyan Kabir",
        "house": "Uttara",
        "study": "Business Study"
    },
    {
        "name": "MD Abdur Rahman",
        "house": "ECB",
        "study": "Sales & Marketing"
    },
    {
        "name": "Anwar",
        "house": "Vashantak",
        "study": None
    }
]

print()
print(type(students))
for i, student in enumerate(students, start=1):
    print(f"{i}. My name is {student['name']} i live in {student['house']} and doing study {student['study']}.")




