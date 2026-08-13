# Question 02 - Bank Account
# Create a bank account using getter and setter.


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance         # Store private balance

    def get_balance(self):
        return self.__balance            # Return balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount      # Update valid balance


account = BankAccount(5000)              # Create account object

print("Balance:", account.get_balance())

account.set_balance(7500)                # Update account balance

print("Updated Balance:", account.get_balance())
