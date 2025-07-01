import json
from datetime import datetime
import os

TASKS_FILE = "tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(TASKS_FILE, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date_str = input("Enter due date (YYYY-MM-DD HH:MM): ")
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date format. Task not added.")
            return
        task = {
            "title": title,
            "description": description,
            "due_date": due_date.isoformat(),
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Pending"
            due_date = datetime.fromisoformat(task["due_date"])
            print(f"{i+1}. {task['title']} | Due: {due_date.strftime('%Y-%m-%d %H:%M')} | {status}")

    def complete_task(self):
        self.view_tasks()
        try:
            index = int(input("Enter task number to mark complete: ")) - 1
            self.tasks[index]["completed"] = True
            self.save_tasks()
            print("Task marked as completed!")
        except (IndexError, ValueError):
            print("Invalid selection.")

    def delete_task(self):
        self.view_tasks()
        try:
            index = int(input("Enter task number to delete: ")) - 1
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Task '{removed['title']}' deleted.")
        except (IndexError, ValueError):
            print("Invalid selection.")

    def edit_task(self):
        self.view_tasks()
        try:
            index = int(input("Enter task number to edit: ")) - 1
            task = self.tasks[index]
            print("Leave field empty to keep unchanged.")
            title = input(f"New title [{task['title']}]: ") or task['title']
            description = input(f"New description [{task['description']}]: ") or task['description']
            due_input = input(f"New due date (YYYY-MM-DD HH:MM) [{task['due_date']}]: ")
            try:
                due_date = datetime.strptime(due_input, "%Y-%m-%d %H:%M").isoformat() if due_input else task['due_date']
            except ValueError:
                print("Invalid date format. Keeping old due date.")
                due_date = task['due_date']
            task.update({"title": title, "description": description, "due_date": due_date})
            self.save_tasks()
            print("Task updated!")
        except (IndexError, ValueError):
            print("Invalid selection.")

if __name__ == '__main__':
    manager = TaskManager()
    while True:
        print("""
SmartTaskCLI Menu:
1. Add Task
2. View Tasks
3. Complete Task
4. Edit Task
5. Delete Task
6. Exit
        """)
        choice = input("Select an option: ")
        if choice == '1':
            manager.add_task()
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            manager.complete_task()
        elif choice == '4':
            manager.edit_task()
        elif choice == '5':
            manager.delete_task()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
