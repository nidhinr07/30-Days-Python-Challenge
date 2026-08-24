students = {}


def load_students():

    try:

        with open("students.txt", "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                try:

                    name, age = line.split("|")

                    students[name] = int(age)

                except ValueError:

                    continue

    except FileNotFoundError:

        pass


def save_students():

    try:

        with open("students.txt", "w") as file:

            for name, age in students.items():

                file.write(f"{name}|{age}\n")

    except OSError:

        print("Unable to save student data.")


def add_student():

    name = input("Enter student name: ").strip()

    if not name:

        print("Student name cannot be empty.")

        return

    for student in students:

        if student.lower() == name.lower():

            print("Student already exists.")

            return

    try:

        age = int(input("Enter student age: "))

        if age <= 0:

            print("Age must be greater than zero.")

            return

        students[name] = age

        save_students()

        print("Student added successfully.")

    except ValueError:

        print("Please enter a valid age.")


def view_students():

    if not students:

        print("No students available.")

        return

    print("\n----- Students -----")

    for number, (name, age) in enumerate(students.items(), start=1):

        print(f"{number}. {name} - Age: {age}")


def find_student(name):

    for student in students:

        if student.lower() == name.lower():

            return student

    return None


def search_student():

    name = input("Enter student name to search: ").strip()

    student = find_student(name)

    if student:

        print(f"Student found: {student} - Age: {students[student]}")

    else:

        print("Student not found.")


def update_student():

    name = input("Enter student name to update: ").strip()

    student = find_student(name)

    if not student:

        print("Student not found.")

        return

    try:

        new_age = int(input("Enter new age: "))

        if new_age <= 0:

            print("Age must be greater than zero.")

            return

        students[student] = new_age

        save_students()

        print("Student updated successfully.")

    except ValueError:

        print("Please enter a valid age.")


def delete_student():

    name = input("Enter student name to delete: ").strip()

    student = find_student(name)

    if student:

        del students[student]

        save_students()

        print("Student deleted successfully.")

    else:

        print("Student not found.")


def show_menu():

    print("\n===== Student Management System =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


load_students()


while True:

    show_menu()

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:

            add_student()

        elif choice == 2:

            view_students()

        elif choice == 3:

            search_student()

        elif choice == 4:

            update_student()

        elif choice == 5:

            delete_student()

        elif choice == 6:

            print("Thank you for using the Student Management System.")

            break

        else:

            print("Please choose a number between 1 and 6.")

    except ValueError:

        print("Please enter a valid number.")
