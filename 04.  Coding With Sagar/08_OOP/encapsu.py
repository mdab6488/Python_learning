print()
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance # Privet Variable

    def deposit(self, ammount):
        self.__balance += ammount
        print(f"Deposited {ammount}. New balance {self.__balance}")

    def get_balance(self):
        return self.__balance # Controlled access

account = BankAccount("12345", 5000)
account.deposit(2000)
print(account.get_balance())

print(account.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'. Did you mean: 'get_balance'?