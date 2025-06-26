print()

def main():
    student = get_student()
    if student['name'] == "Riyan":
        student['house'] = "Uttara Sector 7"
    print(f"{student['name']} from {student['house']}")

# def get_name():
#     return input("Name: ")
#
# def get_house():
#     return input("House: ")

def get_student():
    student = {
        "name": input("Name: ").capitalize(),
        "house": input("House: ").capitalize()
    }
    return student

if __name__ == "__main__":
    main()