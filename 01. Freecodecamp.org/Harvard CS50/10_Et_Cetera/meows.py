
# meows = 3
#
# print()
# for _ in range(meows):
#     print("meow")

class Cat:
    meows = 3

    def meow(self):
        for _ in range(Cat.meows):
            print("meow")

print()
cat = Cat()
cat.meow()