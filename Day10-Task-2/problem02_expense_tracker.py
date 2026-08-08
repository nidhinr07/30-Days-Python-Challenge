# Create an expense tracker using basic Python concepts.
# Store expenses, calculate total, and use recursion.

import math                              # Import math module

expenses = []                            # Store expense details


def add_expense():
    name = input("Enter expense name: ").strip()

    try:
        amount = float(input("Enter expense amount: "))

        if amount < 0:
            raise ValueError("Amount cannot be negative.")

    except ValueError as error:
        print("Invalid amount:", error)
        return

    expense = (name, amount)              # Store expense as tuple
    expenses.append(expense)

    print("Expense added successfully.")


def show_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n---------- Expenses ----------")

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense[0]} - ₹{expense[1]}")


def calculate_total(index=0):
    if index == len(expenses):
        return 0

    return expenses[index][1] + calculate_total(index + 1)


add_expense()
add_expense()

show_expenses()

total = calculate_total()                 # Calculate total recursively

print("\nTotal Expense :", total)
print("Rounded Total :", math.ceil(total))
