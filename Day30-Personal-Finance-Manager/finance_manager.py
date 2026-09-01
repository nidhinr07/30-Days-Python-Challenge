# Day 30 - Personal Finance Manager
# Commit 1 - Add Income, Add Expense and View Records


records = []


def add_income():

    name = input("Enter income source: ").strip()

    amount = float(input("Enter income amount: "))

    record = {
        "type": "Income",
        "name": name,
        "amount": amount
    }

    records.append(record)

    print("Income added successfully.")


def add_expense():

    name = input("Enter expense name: ").strip()

    amount = float(input("Enter expense amount: "))

    record = {
        "type": "Expense",
        "name": name,
        "amount": amount
    }

    records.append(record)

    print("Expense added successfully.")


def view_records():

    if not records:

        print("No records available.")

        return

    print("\n----- Financial Records -----")

    for number, record in enumerate(records, start=1):

        print(
            f"{number}. "
            f"{record['type']} - "
            f"{record['name']} - "
            f"₹{record['amount']:.2f}"
        )


while True:

    print("\n===== Personal Finance Manager =====")

    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Records")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_income()

    elif choice == "2":

        add_expense()

    elif choice == "3":

        view_records()

    elif choice == "4":

        print("Thank you for using Personal Finance Manager.")

        break

    else:

        print("Invalid choice.")
