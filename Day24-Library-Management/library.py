# Day 24 - Library Management System
# Commit 1 - Basic Library


books = []


def add_book():

    book = input("Enter book name: ")

    books.append(book)

    print("Book added successfully.")


def view_books():

    if not books:

        print("No books available.")

        return

    print("\n----- Available Books -----")

    for book in books:

        print(book)


while True:

    print("\n===== Library Management System =====")

    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_book()

    elif choice == "2":

        view_books()

    elif choice == "3":

        print("Thank you for using the library.")

        break

    else:

        print("Invalid choice.")
