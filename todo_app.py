import json
from datetime import datetime

file_name = "tasks.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = input("Enter task title: ")
    date_time = input("Enter date & time (YYYY-MM-DD HH:MM:SS): ")
    tasks = load_tasks()
    tasks.append({"title": title, "date_time": date_time, "done": False})
    save_tasks(tasks)
    print(f"Task '{title}' added!")

def display_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "DONE" if task["done"] else "NOT DONE"
        print(f"{i}- {task['title']} - {task['date_time']} - {status}")

def mark_done():
    display_tasks()
    task_number = int(input("Enter task number to mark as DONE: "))
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number-1]["done"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_number-1]['title']}' marked as DONE!")
    else:
        print("Invalid task number.")

def search_task():
    search = input("Enter title to search: ")
    tasks = load_tasks()
    found = [task for task in tasks if search.lower() in task["title"].lower()]
    if not found:
        print("No tasks found with that title.")
    else:
        for task in found:
            status = "DONE" if task["done"] else "NOT DONE"
            print(f"{task['title']} - {task['date_time']} - {status}")

def menu():
    while True:
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as DONE")
        print("4. Search Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            search_task()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
