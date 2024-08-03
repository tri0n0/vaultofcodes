tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def delete_task(index):
    try:
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task['task']}' deleted.")
    except IndexError:
        print("Invalid task number.")

def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i + 1}. {task['task']} - {status}")

def complete_task(index):
    try:
        tasks[index]["completed"] = True
        print(f"Task '{tasks[index]['task']}' marked as complete.")
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            display_tasks()
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(index)
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            display_tasks()
            index = int(input("Enter the task number to mark as complete: ")) - 1
            complete_task(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
