# docs.python.org/3/library/csv.html
import csv

print()

# students = []
# with open("students_with.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({
#             "name": name,
#             "home": home
#         })
#
# for student in sorted(students, key=lambda std: std["name"]):
#     print(f"{student['name']} is from {student['home']}")

students = []
with open("students_with.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "name": row["name"],
            "home": row["home"],
            "study": row["study"]
        })

for student in sorted(students, key=lambda std: std["name"]):
    print(f"{student['name']} is from {student['home']} studying {student['study']}")

