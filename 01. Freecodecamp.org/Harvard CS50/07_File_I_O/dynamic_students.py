import csv

print()
name = input("What's your name? ")
home = input("Where's your home? ")

# with open("for_dynamic_student.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

with open("for_dynamic_student.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({
        "name": name,
        "home": home
    })