from task_manager import TaskManager
from utils import clear_screen

def display_menu():
    """Display the main menu options."""
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def main():
    """Main function to run the application loop."""
    task_manager = TaskManager()
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-4).")
        
        input("\nPress Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    main()
