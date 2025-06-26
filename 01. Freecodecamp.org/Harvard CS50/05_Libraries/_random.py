# import random
#
# coin = random.choice(["Heads", "Tails"])
#
# print()
# print(coin)

from random import choice, randint, shuffle

coin = choice(["Heads", "Tails"])

print()
print(coin)

print()
number = randint(1, 10)
print(number)

print()
cards = ["Jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)