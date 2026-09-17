tasks = []


def add_task():
    subject = input("Enter subject: ")
    task = input("Enter study task: ")

    tasks.append({
        "subject": subject,
        "task": task,
        "completed": False
    })

    print("Task added successfully!\n")


def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    print("\n--- YOUR STUDY TASKS ---")

    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"{number}. {task['subject']} - {task['task']} [{status}]")

    print()


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a number.\n")


def main():
    while True:
        print("===== STUDENT STUDY PLANNER =====")
        print("1. Add study task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            print("Good luck with your studies!")
            break

        else:
            print("Invalid choice. Try again.\n")


main()