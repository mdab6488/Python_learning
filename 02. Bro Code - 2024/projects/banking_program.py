def show_balance(balance):
    print(f"Your balance is {balance:.2f}\n")

def deposit():
    ammount = float(input("Enter an ammount to be deposited: "))

    if ammount < 0:
        print("*" * 30)
        print("Thay's not a valid ammount\n")
        print("*" * 30)
        return 0
    else:
        return ammount
def withdraw(balance):
    ammount = float(input("Enter an ammount to be withdraw: "))

    if ammount > balance:
        print("*" * 30)
        print("Insufficient Funds\n")
        print("*" * 30)
        return 0
    elif ammount < 0:
        print("*" * 30)
        print("Ammount must be greater than 0\n")
        print("*" * 30)
        return 0
    else:
        return ammount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*" * 30)
        print(f"{' ' * 5} Banking Program {' ' * 5} ")
        print("*" * 30)
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*" * 30)

        choice = input("Enter your choice (1-4): ")
        print("-" * 30)

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*" * 30)
            print("That is not a valid choice ❌")
            print("*" * 30)
    print("Thank you have a nice day! 😍")
    print("*" * 30)

if __name__ == '__main__':
    main()