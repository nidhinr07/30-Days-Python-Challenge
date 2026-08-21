# Day 23 - Contact Book


contacts = {}


def add_contact():

    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone

    print("Contact added successfully.")


def view_contacts():

    if not contacts:

        print("No contacts found.")

        return

    print("\n----- Contacts -----")

    for name, phone in contacts.items():

        print(name, ":", phone)


def search_contact():

    name = input("Enter name to search: ")

    if name in contacts:

        print("Phone:", contacts[name])

    else:

        print("Contact not found.")


def delete_contact():

    name = input("Enter name to delete: ")

    if name in contacts:

        del contacts[name]

        print("Contact deleted.")

    else:

        print("Contact not found.")


while True:

    print("\n----- Contact Book -----")

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact()

        elif choice == 2:
            view_contacts()

        elif choice == 3:
            search_contact()

        elif choice == 4:
            delete_contact()

        elif choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

    except ValueError:

        print("Please enter a number.")
