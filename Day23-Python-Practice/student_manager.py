# Day 23 - Student Manager


students = {}


def add_student():

    name = input("Enter student name: ")

    try:

        marks = float(input("Enter student marks: "))

        if 0 <= marks <= 100:

            students[name] = marks

            print("Student added successfully.")

        else:

            print("Marks must be between 0 and 100.")

    except ValueError:

        print("Please enter valid marks.")


def view_students():

    if not students:

        print("No students found.")

        return

    print("\n----- Students -----")

    for name, marks in students.items():

        print(name, ":", marks)


def search_student():

    name = input("Enter student name: ")

    if name in students:

        print("Marks:", students[name])

    else:

        print("Student not found.")


def calculate_average():

    if not students:

        print("No marks available.")

        return

    average = sum(students.values()) / len(students)

    print("Average Marks:", average)


while True:

    print("\n----- Student Manager -----")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Exit")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            calculate_average()

        elif choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

    except ValueError:

        print("Please enter a number.")
