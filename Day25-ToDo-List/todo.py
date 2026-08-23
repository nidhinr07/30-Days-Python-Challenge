# Day 25 - To-Do List Manager
# Commit 1 - Basic To-Do List


tasks = []


def add_task():

    task = input("Enter task: ")

    tasks.append(task)

    print("Task added successfully.")


def view_tasks():

    if not tasks:

        print("No tasks available.")

        return

    print("\n----- To-Do List -----")

    for task in tasks:

        print(task)


while True:

    print("\n===== To-Do List Manager =====")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_task()

    elif choice == "2":

        view_tasks()

    elif choice == "3":

        print("Thank you for using the To-Do List.")

        break

    else:

        print("Invalid choice.")
