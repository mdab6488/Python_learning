print()

def main():
    name, house = get_student()
    print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")
#
# def get_house():
#     return input("House: ")

def get_student():
    name = input("Name: ")
    hosue = input("House: ")
    # checking = name, hosue
    # print(type(checking)) # <class 'tuple'>
    return name, hosue

if __name__ == "__main__":
    main()