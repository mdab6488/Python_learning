
print()

# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

# with open("students.csv") as file:
#     for line in sorted(file):
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {
            "name": name,
            "house": house
        }
        students.append(student)

# def get_name(std):
#     return std["name"]
#
# def get_house(std):
#     return std["house"]
#
# for student in sorted(students, key=get_name, reverse=False):
#     print(f"{student['name']} is in {student['house']}")

for student in sorted(students, key=lambda studnet: studnet["name"], reverse=False):
    print(f"{student['name']} is in {student['house']}")

# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")
#
# for student in sorted(students):
#     print(student)

