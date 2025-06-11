
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print(f"{"-" * 5} YOUR CART {"-" * 5}")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
    # print(total, end=" ")

print(f"\nYour total is: ${total}")

print(f"{"-" * 15}")