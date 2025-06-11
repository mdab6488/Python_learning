import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*" * 30)
    print(f"{' ' * 8}{' | '.join(row)}{' ' * 8}")
    print("*" * 30)

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0

def main():
    balance = 100

    print("*" * 30)
    print(f"{' ' * 3}Welcome to Python Slots{' ' * 3}")
    print(f"{' ' * 4}Symbols: 🍒🍉🍋🔔⭐{' ' * 4}")
    print("*" * 30)

    while balance > 0:
        print(f"💲 Current balance: ${balance}")

        bet = input("🤑 Place your bet ammount: ")

        if not bet.isdigit():
            print("-" * 30)
            print("❌ Please enter a valid number")
            print("-" * 30)
            continue

        bet = int(bet)

        if bet > balance:
            print("-" * 30)
            print("❌ Insufficient Funds")
            print("-" * 30)
            continue

        if bet <= 0:
            print("-" * 30)
            print("❌ Bet must be greather than 0")
            print("-" * 30)
            continue

        balance -= bet

        row = spin_row()
        print("Spinning..")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"💸💸💸You won ${payout}")
            print("💹" * 30)
        else:
            print("🥲 Sorry you lost this round")
            print("-" * 30)

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != "Y":
            break
    print("*" * 30)
    print(f"✅ Game over! \nYour final 💲balance is ${balance}")
    print("*" * 30)

if __name__ == '__main__':
    main()