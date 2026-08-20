# Day 22 - Expense Tracker


def add_expense():

    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter expense amount: "))

        with open("expenses.txt", "a") as file:
            file.write(f"{name},{amount}\n")

        print("Expense added successfully.")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():

    try:

        with open("expenses.txt", "r") as file:

            expenses = file.readlines()

            if not expenses:
                print("No expenses found.")
                return

            total = 0

            print("\n----- Expenses -----")

            for expense in expenses:

                name, amount = expense.strip().split(",")

                print(name, ":", amount)

                total += float(amount)

            print("\nTotal:", total)

    except FileNotFoundError:
        print("No expense file found.")


add_expense()

view_expenses()
