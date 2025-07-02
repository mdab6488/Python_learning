print()
class Character:
    def __init__(self, name, health, attack, blood):
        self.name = name
        self.health = health
        self.attack = attack
        self.blood = blood

    def attack_enime(self):
        print(f"{self.name} attacks with power {self.attack} {self.blood}")

warrior = Character("Thor", 100, 50, "Red")
mage = Character("Loki", 80, 70, "Black")
archer = Character("Archer", 80, 90, "White")

warrior.attack_enime()
mage.attack_enime()
archer.attack_enime()

