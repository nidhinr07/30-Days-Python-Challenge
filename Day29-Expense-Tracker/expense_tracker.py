expenses = []

def load_expenses():

    try:

        with open("expenses.txt", "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                try:

                    name, amount = line.split("|")

                    expenses.append({
                        "name": name,
                        "amount": float(amount)
                    })

                except ValueError:

                    continue

    except FileNotFoundError:

        pass


def save_expenses():

    try:

        with open("expenses.txt", "w") as file:

            for expense in expenses:

                file.write(
                    f"{expense['name']}|"
                    f"{expense['amount']}\n"
                )

    except OSError:

        print("Unable to save expense data.")


def add_expense():

    name = input(
        "Enter expense name: "
    ).strip()

    if not name:

        print("Expense name cannot be empty.")

        return

    try:

        amount = float(
            input("Enter expense amount: ")
        )

        if amount <= 0:

            print("Amount must be greater than zero.")

            return

    except ValueError:

        print("Please enter a valid amount.")

        return

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)

    save_expenses()

    print("Expense added successfully.")


def view_expenses():

    if not expenses:

        print("No expenses available.")

        return

    print("\n----- Expenses -----")

    for number, expense in enumerate(
        expenses,
        start=1
    ):

        print(
            f"{number}. "
            f"{expense['name']} - "
            f"₹{expense['amount']:.2f}"
        )


def search_expense():

    name = input(
        "Enter expense name to search: "
    ).strip()

    found = False

    for expense in expenses:

        if expense["name"].lower() == name.lower():

            print(
                f"Found: {expense['name']} - "
                f"₹{expense['amount']:.2f}"
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
            input(
                "Enter expense number to delete: "
            )
        )

        if 1 <= number <= len(expenses):

            removed = expenses.pop(number - 1)

            save_expenses()

            print(
                f"Deleted: {removed['name']} - "
                f"₹{removed['amount']:.2f}"
            )

        else:

            print("Invalid expense number.")

    except ValueError:

        print("Please enter a valid number.")


def calculate_total():

    total = 0

    for expense in expenses:

        total += expense["amount"]

    print(
        f"\nTotal expenses: ₹{total:.2f}"
    )


def show_menu():

    print("\n===== Expense Tracker =====")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Calculate Total")
    print("6. Exit")


load_expenses()


while True:

    show_menu()

    try:

        choice = int(
            input("Enter your choice: ")
        )

        if choice == 1:

            add_expense()

        elif choice == 2:

            view_expenses()

        elif choice == 3:

            search_expense()

        elif choice == 4:

            delete_expense()

        elif choice == 5:

            calculate_total()

        elif choice == 6:

            print(
                "Thank you for using the Expense Tracker."
            )

            break

        else:

            print(
                "Please choose a number between 1 and 6."
            )

    except ValueError:

        print("Please enter a valid number.")
