# Day 24 - Library Management System
# Commit 2 - Search and Remove Books


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


def search_book():

    book = input("Enter book name to search: ")

    if book in books:

        print("Book is available.")

    else:

        print("Book not found.")


def remove_book():

    book = input("Enter book name to remove: ")

    if book in books:

        books.remove(book)

        print("Book removed successfully.")

    else:

        print("Book not found.")


while True:

    print("\n===== Library Management System =====")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_book()

    elif choice == "2":

        view_books()

    elif choice == "3":

        search_book()

    elif choice == "4":

        remove_book()

    elif choice == "5":

        print("Thank you for using the library.")

        break

    else:

        print("Invalid choice.")
