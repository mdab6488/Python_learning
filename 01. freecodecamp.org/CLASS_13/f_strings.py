person = "MD ABDUR RAHMAN"
coins = 3

# print("\n" + person + " has " + str(coins) + " coins left.")

# message = "\n%s has %s coinns left." % (person, coins)
# print(message)


# message = "\n{} has {} coins left.".format(person, coins)
# print(message)


# message = "\n{person} has {coins} coins left.".format(coins=coins, person=person)

# print(message)

# player = {"person": "MD ABDUR RAHMAN", "coins": 3}
# message = "\n{person} has {coins} coins left.".format(**player)

# print(message)

################################################
# message = f"Hello, {person}. You have {coins} coins in your pocket."
# print(message)

# message = f"Hello, {person.lower()}. You have {2 * 5} coins in your pocket."
# print(message)


# player = {"person": "MD ABDUR RAHMAN", "coins": 3}
# message = f"Hello, {player['person']}. You have {2 * 5} coins in your pocket."
# print(message)


################################################
# You can pass fromatting options

# num = 10
# print(f"\n 2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"\n 2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")
