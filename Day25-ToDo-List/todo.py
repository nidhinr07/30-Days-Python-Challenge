# Day 25 - To-Do List Manager
# Commit 3 - File Handling


tasks = []


def load_tasks():

    try:

        with open("tasks.txt", "r") as file:

            for line in file:

                task, status = line.strip().split("|")

                tasks.append({
                    "task": task,
                    "completed": status == "True"
                })

    except FileNotFoundError:

        pass


def save_tasks():

    with open("tasks.txt", "w") as file:

        for item in tasks:

            file.write(
                f"{item['task']}|{item['completed']}\n"
            )


def add_task():

    task = input("Enter task: ").strip()

    if not task:

        print("Task cannot be empty.")

        return

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks()

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

            save_tasks()

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

            save_tasks()

            print(f"Deleted: {removed_task['task']}")

        else:

            print("Invalid task number.")

    except ValueError:

        print("Please enter a valid number.")


# Load saved tasks when program starts
load_tasks()


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
