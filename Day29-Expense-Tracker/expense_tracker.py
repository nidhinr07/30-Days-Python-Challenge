# Day 29 - Expense Tracker
# Commit 2 - Search, Delete and Calculate Total


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


def search_expense():

    name = input("Enter expense name to search: ").strip()

    found = False

    for expense in expenses:

        if expense["name"].lower() == name.lower():

            print(
                f"Found: {expense['name']} "
                f"- ₹{expense['amount']:.2f}"
            )

            found = True

    if not found:

        print("Expense not found.")


def delete_expense():

    view_expenses()

    if not expenses:
        return

    try:

        number = int(
            input("Enter expense number to delete: ")
        )

        if 1 <= number <= len(expenses):

            removed = expenses.pop(number - 1)

            print(
                f"Deleted: {removed['name']} "
                f"- ₹{removed['amount']:.2f}"
            )

        else:

            print("Invalid expense number.")

    except ValueError:

        print("Please enter a valid number.")


def calculate_total():

    total = 0

    for expense in expenses:

        total += expense["amount"]

    print(f"\nTotal expenses: ₹{total:.2f}")


while True:

    print("\n===== Expense Tracker =====")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Calculate Total")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_expense()

    elif choice == "2":

        view_expenses()

    elif choice == "3":

        search_expense()

    elif choice == "4":

        delete_expense()

    elif choice == "5":

        calculate_total()

    elif choice == "6":

        print("Thank you for using the Expense Tracker.")

        break

    else:

        print("Invalid choice.")
