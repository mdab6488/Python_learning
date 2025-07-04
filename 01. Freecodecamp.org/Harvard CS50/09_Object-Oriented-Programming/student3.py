print()

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Uttara", "Ecb", "Vashantak", "Matikata"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ").capitalize()
    house = input("House: ").capitalize()
    return Student(name, house)

if __name__ == "__main__":
    main()