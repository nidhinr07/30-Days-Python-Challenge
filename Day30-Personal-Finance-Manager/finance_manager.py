records = []

def load_records():

    try:

        with open("finance_records.txt", "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                try:

                    record_type, name, amount = line.split("|")

                    records.append({
                        "type": record_type,
                        "name": name,
                        "amount": float(amount)
                    })

                except ValueError:

                    continue

    except FileNotFoundError:

        pass


def save_records():

    try:

        with open("finance_records.txt", "w") as file:

            for record in records:

                file.write(
                    f"{record['type']}|"
                    f"{record['name']}|"
                    f"{record['amount']}\n"
                )

    except OSError:

        print("Unable to save financial records.")


def add_income():

    name = input(
        "Enter income source: "
    ).strip()

    if not name:

        print("Income source cannot be empty.")

        return

    try:

        amount = float(
            input("Enter income amount: ")
        )

        if amount <= 0:

            print("Amount must be greater than zero.")

            return

    except ValueError:

        print("Please enter a valid amount.")

        return

    record = {
        "type": "Income",
        "name": name,
        "amount": amount
    }

    records.append(record)

    save_records()

    print("Income added successfully.")


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

    record = {
        "type": "Expense",
        "name": name,
        "amount": amount
    }

    records.append(record)

    save_records()

    print("Expense added successfully.")


def view_records():

    if not records:

        print("No records available.")

        return

    print("\n----- Financial Records -----")

    for number, record in enumerate(
        records,
        start=1
    ):

        print(
            f"{number}. "
            f"{record['type']} - "
            f"{record['name']} - "
            f"₹{record['amount']:.2f}"
        )


def search_record():

    name = input(
        "Enter record name to search: "
    ).strip()

    found = False

    for record in records:

        if record["name"].lower() == name.lower():

            print(
                f"Found: {record['type']} - "
                f"{record['name']} - "
                f"₹{record['amount']:.2f}"
            )

            found = True

    if not found:

        print("Record not found.")


def delete_record():

    view_records()

    if not records:

        return

    try:

        number = int(
            input(
                "Enter record number to delete: "
            )
        )

        if 1 <= number <= len(records):

            removed = records.pop(number - 1)

            save_records()

            print(
                f"Deleted: {removed['type']} - "
                f"{removed['name']} - "
                f"₹{removed['amount']:.2f}"
            )

        else:

            print("Invalid record number.")

    except ValueError:

        print("Please enter a valid number.")


def calculate_balance():

    total_income = 0
    total_expense = 0

    for record in records:

        if record["type"] == "Income":

            total_income += record["amount"]

        else:

            total_expense += record["amount"]

    balance = total_income - total_expense

    print("\n----- Financial Summary -----")

    print(f"Total Income: ₹{total_income:.2f}")
    print(f"Total Expenses: ₹{total_expense:.2f}")
    print(f"Current Balance: ₹{balance:.2f}")


def show_menu():

    print("\n===== Personal Finance Manager =====")

    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Records")
    print("4. Search Record")
    print("5. Delete Record")
    print("6. Calculate Balance")
    print("7. Exit")


load_records()


while True:

    show_menu()

    try:

        choice = int(
            input("Enter your choice: ")
        )

        if choice == 1:

            add_income()

        elif choice == 2:

            add_expense()

        elif choice == 3:

            view_records()

        elif choice == 4:

            search_record()

        elif choice == 5:

            delete_record()

        elif choice == 6:

            calculate_balance()

        elif choice == 7:

            print(
                "Thank you for using "
                "Personal Finance Manager."
            )

            break

        else:

            print(
                "Please choose a number between 1 and 7."
            )

    except ValueError:

        print("Please enter a valid number.")
