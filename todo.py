import json
import os


TASKS_FILE = 'tasks.json'


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {description}")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            status = "✔" if task["completed"]else "✘"
            print(f"{index + 1}. {task['description']} [{status}]")


def complete_task(tasks, task_number):
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        save_tasks(tasks)
        print(f"Task marked as completed: {tasks[task_number]['description']}")
    else:
        print("Invalid task number.")

def delete_task(tasks, task_number):
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        save_tasks(tasks)
        print(f"Task deleted: {removed_task['description']}")
    else:
        print("Invalid task number.")
       

def display_menu():
    print("\nTodo List CLI")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '3':
            view_tasks(tasks)
            task_number = int(input("Enter task number to mark as completed: ")) - 1
            complete_task(tasks, task_number)
        elif choice == '4':
            view_tasks(tasks)
            task_number = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, task_number)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()      