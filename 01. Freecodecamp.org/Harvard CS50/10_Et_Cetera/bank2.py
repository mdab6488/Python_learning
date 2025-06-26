class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, ammount):
        self._balance += ammount

    def withdraw(self, ammount):
        self._balance -= ammount

def main():
    print()
    account = Account()
    print(f"Blance: {account.balance}")
    account.deposit(100)
    account.withdraw(50)
    print(f"Blance: {account.balance}")

if __name__ == "__main__":
    main()