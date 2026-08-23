tasks = []


def load_tasks():

    try:

        with open("tasks.txt", "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                try:

                    task, status = line.split("|")

                    tasks.append({
                        "task": task,
                        "completed": status == "True"
                    })

                except ValueError:

                    continue

    except FileNotFoundError:

        pass


def save_tasks():

    try:

        with open("tasks.txt", "w") as file:

            for item in tasks:

                file.write(
                    f"{item['task']}|{item['completed']}\n"
                )

    except OSError:

        print("Unable to save tasks.")


def add_task():

    task = input("Enter task: ").strip()

    if not task:

        print("Task cannot be empty.")

        return

    for item in tasks:

        if item["task"].lower() == task.lower():

            print("Task already exists.")

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

            if tasks[number - 1]["completed"]:

                print("Task is already completed.")

            else:

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


def show_menu():

    print("\n===== To-Do List Manager =====")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


load_tasks()


while True:

    show_menu()

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:

            add_task()

        elif choice == 2:

            view_tasks()

        elif choice == 3:

            complete_task()

        elif choice == 4:

            delete_task()

        elif choice == 5:

            print("Thank you for using the To-Do List.")

            break

        else:

            print("Please choose a number between 1 and 5.")

    except ValueError:

        print("Please enter a valid number.")
