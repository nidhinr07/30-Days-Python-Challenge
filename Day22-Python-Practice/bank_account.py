# Day 22 - Bank Account


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

        print("Amount deposited successfully.")

    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

            print("Amount withdrawn successfully.")

        else:

            print("Insufficient balance.")

    def show_balance(self):

        print("Account Holder:", self.name)
        print("Balance:", self.balance)


account = BankAccount("Alex", 5000)

account.show_balance()

account.deposit(1000)

account.withdraw(2000)

account.show_balance()
