print()
num_1 = float(input("Enter Number 1 = "))
num_2 = float(input("Enter Number 2 = "))

user_choice = input("Enter your choice (+ - *) : ")

if user_choice == "+":
    print(f"Addition: {num_1 + num_2}")
elif user_choice == "-":
    print(f"Subtraction: {num_1 - num_2}")
elif user_choice == "*":
    print(f"Multification: {num_1 * num_2}")
else:
    print("Invalid choice")