import random

# print(help(random))

low = 1
high = 20
options = ("rock", "paper", "scissor")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, high)
# number = random.random()
# number = random.choice(options)
random.shuffle(cards)

print(cards)
# print(number)