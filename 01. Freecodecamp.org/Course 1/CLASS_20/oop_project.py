from bank_accounts import BankAccount, InterestRewardsAcct, SavingsAcct

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

print("-----------------------------------------------")

Dave.deposit(500)
Sara.deposit(1000)

print("-----------------------------------------------")

Dave.withdraw(20000)
Dave.withdraw(10)

print("-----------------------------------------------")

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)

print("-----------------------------------------------")
jim = InterestRewardsAcct(1000, "Jim")
jim.getBalance()

jim.deposit(100)
jim.transfer(100, Dave)

print("-----------------------------------------------")

Blaze = SavingsAcct(1000, "Blaze")
Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)
# print("-----------------------------------------------")
