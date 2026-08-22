books = []


def load_books():

    try:

        with open("books.txt", "r") as file:

            for line in file:

                books.append(line.strip())

    except FileNotFoundError:

        pass


def add_book():

    book = input("Enter book name: ")

    books.append(book)

    with open("books.txt", "a") as file:

        file.write(book + "\n")

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

        with open("books.txt", "w") as file:

            for item in books:

                file.write(item + "\n")

        print("Book removed successfully.")

    else:

        print("Book not found.")


# Load saved books when program starts
load_books()


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
