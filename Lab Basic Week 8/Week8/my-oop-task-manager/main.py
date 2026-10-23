# my-oop-task-manager/main.py
import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from task_manager import TaskManager

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'tasks.json')


def ask_task_id(prompt):
    """Ask the user for a task ID. Returns an int, or None if invalid."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return None


def main():
    manager = TaskManager(DATA_FILE)

    while True:
        print("\n--- OOP Task Manager Menu ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            manager.add_task(input("Enter task description: "))
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            task_id = ask_task_id("Enter task ID to mark complete: ")
            if task_id is not None:
                manager.complete_task(task_id)
        elif choice == '4':
            task_id = ask_task_id("Enter task ID to delete: ")
            if task_id is not None:
                manager.delete_task(task_id)
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
