balance = 0

def main():
    print()
    print(f"Balance: {balance}")
    deposit(100)
    widthdraw(50)
    print(f"Balance: {balance}")

def deposit(ammount):
    global balance
    balance += ammount

def widthdraw(ammount):
    global balance
    balance -= ammount

if __name__ == "__main__":
    main()