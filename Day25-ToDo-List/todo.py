# Day 25 - To-Do List Manager
# Commit 2 - Complete and Delete Tasks


tasks = []


def add_task():

    task = input("Enter task: ").strip()

    tasks.append({
        "task": task,
        "completed": False
    })

    print("Task added successfully.")


def view_tasks():

    if not tasks:

        print("No tasks available.")

        return

    print("\n----- To-Do List -----")

    for index, item in enumerate(tasks, start=1):

        status = "Completed" if item["completed"] else "Pending"

        print(f"{index}. {item['task']} - {status}")


def complete_task():

    view_tasks()

    if not tasks:
        return

    try:

        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):

            tasks[number - 1]["completed"] = True

            print("Task marked as completed.")

        else:

            print("Invalid task number.")

    except ValueError:

        print("Please enter a valid number.")


def delete_task():

    view_tasks()

    if not tasks:
        return

    try:

        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):

            removed_task = tasks.pop(number - 1)

            print(f"Deleted: {removed_task['task']}")

        else:

            print("Invalid task number.")

    except ValueError:

        print("Please enter a valid number.")


while True:

    print("\n===== To-Do List Manager =====")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_task()

    elif choice == "2":

        view_tasks()

    elif choice == "3":

        complete_task()

    elif choice == "4":

        delete_task()

    elif choice == "5":

        print("Thank you for using the To-Do List.")

        break

    else:

        print("Invalid choice.")
