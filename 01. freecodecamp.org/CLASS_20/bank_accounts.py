class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' Created. \nBalance: ${self.balance:.2f} ")

    def getBalance(self):
        print(f"Account '{self.name}' balance = ${self.balance:.2f} ")

    def deposit(self, ammount):
        self.balance = self.balance + ammount
        print("\nDeposit Complete.")
        self.getBalance()

    def viableTransaction(self, ammount):
        if self.balance >= ammount:
            return
        else:
            raise BalanceException(
                f"Insufficient funds. Your balance is ${self.balance:.2f} and you are trying to withdraw ${ammount:.2f}."
            )

    def withdraw(self, ammount):
        try:
            self.viableTransaction(ammount)
            self.balance = self.balance - ammount
            print("Withdrawal Complete.")
            self.getBalance()
        except BalanceException as e:
            print(f"Withdraw interrrupted: {e}")

    def transfer(self, ammount, otherAccount):
        try:
            print("\n******************************\nBeginning Transfer..🚀\n")
            self.viableTransaction(ammount)
            self.withdraw(ammount)
            otherAccount.deposit(ammount)
            print("\nTransfer Complete! ✅\n******************************")

            # self.balance = self.balance - ammount
            # otherAccount.balance = otherAccount.balance + ammount
            # print(
            #     f"Transfer Complete. ${ammount:.2f} transferred from '{self.name}' to '{otherAccount.name}'"
            # )
            # self.getBalance()
            # otherAccount.getBalance()
        except BalanceException as e:
            print(f"Transfer interrupted: {e} ❌")


class InterestRewardsAcct(BankAccount):
    def deposit(self, ammount):
        self.balance = self.balance + (ammount * 1.05)
        print("\nDeposit Complete.")
        self.getBalance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.interestRate = 5

    def withdraw(self, ammount):
        try:
            self.viableTransaction(ammount + self.interestRate)
            self.balance = self.balance - (ammount + self.interestRate)
            print("\nWithdraw comppleted.")
            self.getBalance()
        except BalanceException as e:
            print(f"Withdraw interrupted: {e}")
