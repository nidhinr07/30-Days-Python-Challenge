# Day 29 - Expense Tracker
# Commit 1 - Add and View Expenses


expenses = []


def add_expense():

    name = input("Enter expense name: ").strip()

    amount = float(input("Enter expense amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully.")


def view_expenses():

    if not expenses:

        print("No expenses available.")

        return

    print("\n----- Expenses -----")

    for number, expense in enumerate(expenses, start=1):

        print(
            f"{number}. "
            f"{expense['name']} - ₹{expense['amount']:.2f}"
        )


while True:

    print("\n===== Expense Tracker =====")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_expense()

    elif choice == "2":

        view_expenses()

    elif choice == "3":

        print("Thank you for using the Expense Tracker.")

        break

    else:

        print("Invalid choice.")
