print()

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ").capitalize()
        house = input("House: ").capitalize()
        return cls(name, house)


def main():
    print(Student.get())

if __name__ == "__main__":
    main()