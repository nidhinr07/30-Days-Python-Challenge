books = []

def load_books():

    try:

        with open("books.txt", "r") as file:

            for line in file:

                book = line.strip()

                if book:
                    books.append(book)

    except FileNotFoundError:

        pass


def add_book():

    book = input("Enter book name: ").strip()

    if not book:

        print("Book name cannot be empty.")

        return

    books.append(book)

    with open("books.txt", "a") as file:

        file.write(book + "\n")

    print("Book added successfully.")


def view_books():

    if not books:

        print("No books available.")

        return

    print("\n----- Available Books -----")

    for index, book in enumerate(books, start=1):

        print(f"{index}. {book}")


def search_book():

    book = input("Enter book name to search: ").strip()

    for item in books:

        if item.lower() == book.lower():

            print("Book is available.")

            return

    print("Book not found.")


def remove_book():

    book = input("Enter book name to remove: ").strip()

    for item in books:

        if item.lower() == book.lower():

            books.remove(item)

            with open("books.txt", "w") as file:

                for saved_book in books:

                    file.write(saved_book + "\n")

            print("Book removed successfully.")

            return

    print("Book not found.")


def show_menu():

    print("\n===== Library Management System =====")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")


load_books()


while True:

    show_menu()

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:

            add_book()

        elif choice == 2:

            view_books()

        elif choice == 3:

            search_book()

        elif choice == 4:

            remove_book()

        elif choice == 5:

            print("Thank you for using the library.")

            break

        else:

            print("Please choose a number between 1 and 5.")

    except ValueError:

        print("Please enter a valid number.")
