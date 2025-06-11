print()

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

a = Programmer(name="MD ABDUR RAHMAN", salary=1000000, pin=123456)
print(a.name, a.salary, a.pin, a.company)

print()
r = Programmer(name="Riyan", salary=2000000, pin=123456)
print(r.name, r.salary, r.pin, r.company)

