# Day 08 - Raising Custom Exceptions

# -----------------------------------
# Raising a ValueError
# -----------------------------------

age = int(input("Enter your age: "))          # Get user age

if age < 18:
    raise ValueError("Age must be 18 or above.")

print("You are eligible.")


# -----------------------------------
# Raising a Custom Error
# -----------------------------------

balance = 500                                # Account balance
amount = int(input("\nEnter withdrawal amount: "))

if amount > balance:
    raise Exception("Insufficient balance.")

print("Transaction successful.")
