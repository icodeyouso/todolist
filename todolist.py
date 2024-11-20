def display_menu():
    """Display the main menu."""
    print("\nWelcome to the To-Do List Application")
    print("Please select an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")


def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task description: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Task description cannot be empty.")


def view_tasks(tasks):
    """View all tasks in the list."""
    if tasks:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks to display.")


def delete_task(tasks):
    """Delete a task from the list."""
    if tasks:
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to delete.")


def main():
    """Main function to run the To-Do list application."""
    tasks = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                print("Thank you for using the To-Do List Application. Goodbye!")
                break
            else:
                print("Please enter a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
        finally:
            print("\nReturning to main menu...")


if __name__ == "__main__":
    main()