class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        """Add a new task to the list."""
        task = input("Enter the task: ").strip()
        if task:
            self.tasks.append(task)
            print(f"Task added: {task}")
        else:
            print("Task cannot be empty!")

    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def delete_task(self):
        """Delete a task from the list."""
        if not self.tasks:
            print("No tasks to delete.")
            return
        
        self.view_tasks()
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(self.tasks):
                removed_task = self.tasks.pop(task_num - 1)
                print(f"Task removed: {removed_task}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
