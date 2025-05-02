menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print(f"{"-" * 7} MENU {"-" * 7}")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print(f"{"-" * 20}")

while True:
    food = input("Sellect an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

# print(cart)
print(f"{"-" * 4} YOUR ORDER {"-" * 4}")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")