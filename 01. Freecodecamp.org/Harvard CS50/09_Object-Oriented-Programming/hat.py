import random

print()

class Hat:
    houses = ["Uttara", "ECB", "Matikata", "Vashantak"]

    @classmethod
    def sort(cls, name):
        print(f"{name} is in, {random.choice(cls.houses)}")

Hat.sort("Riyan")
