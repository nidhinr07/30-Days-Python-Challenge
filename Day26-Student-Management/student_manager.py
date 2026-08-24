# Day 26 - Student Management System
# Commit 1 - Basic Student Management


students = {}


def add_student():

    name = input("Enter student name: ")
    age = input("Enter student age: ")

    students[name] = age

    print("Student added successfully.")


def view_students():

    if not students:

        print("No students available.")

        return

    print("\n----- Students -----")

    for name, age in students.items():

        print("Name:", name)
        print("Age:", age)
        print()


while True:

    print("\n===== Student Management System =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        print("Thank you for using the Student Management System.")

        break

    else:

        print("Invalid choice.")
