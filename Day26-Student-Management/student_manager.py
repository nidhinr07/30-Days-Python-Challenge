# Day 26 - Student Management System
# Commit 2 - Search, Update and Delete


students = {}


def add_student():

    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()

    students[name] = age

    print("Student added successfully.")


def view_students():

    if not students:

        print("No students available.")

        return

    print("\n----- Students -----")

    for number, (name, age) in enumerate(students.items(), start=1):

        print(f"{number}. {name} - Age: {age}")


def search_student():

    name = input("Enter student name to search: ").strip()

    if name in students:

        print(f"Student found: {name} - Age: {students[name]}")

    else:

        print("Student not found.")


def update_student():

    name = input("Enter student name to update: ").strip()

    if name in students:

        new_age = input("Enter new age: ").strip()

        students[name] = new_age

        print("Student updated successfully.")

    else:

        print("Student not found.")


def delete_student():

    name = input("Enter student name to delete: ").strip()

    if name in students:

        del students[name]

        print("Student deleted successfully.")

    else:

        print("Student not found.")


while True:

    print("\n===== Student Management System =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        update_student()

    elif choice == "5":

        delete_student()

    elif choice == "6":

        print("Thank you for using the Student Management System.")

        break

    else:

        print("Invalid choice.")
