friends = {}

print()
for friend in range(4):
    numbers = friend + 1
    name = input(f"Enter friends name {numbers}: ")
    lang = input(f"What subject he/she learning {numbers}: ")
    friends.update({name: lang})

print("*" * 30)
for friend in friends.items():
    print(friend)