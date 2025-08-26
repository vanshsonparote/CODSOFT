# ----- To-Do List Application -----

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks yet! Add some tasks first.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✔ Done" if task['done'] else "✘ Not Done"
            print(f"{i}. {task['title']} [{status}]")
        print()

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added successfully!\n")

def mark_done():
    show_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to mark as done: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]['done'] = True
                print("Task marked as done!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Enter a valid number!\n")

def delete_task():
    show_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                tasks.pop(task_no - 1)
                print("Task deleted!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Enter a valid number!\n")

def main():
    while True:
        print("----- TO-DO LIST MENU -----")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
