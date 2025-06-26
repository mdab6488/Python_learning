# *args, **kwargs
print()
# first, _ = input("What's your name? ").split(" ")
# print(f"Hello, {first}")

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]
# # print(total(coins[0], coins[1], coins[2]), "Knuts")
# print(total(*coins), "Knuts")

coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
print(total(**coins), "Knuts")