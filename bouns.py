import json
from datetime import datetime

file_name = "to_do.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = input("Enter task title: ")
    date_time = input("Enter date & time (YYYY-MM-DD HH:MM:SS): ")
    task = {
        "title": title,
        "date_time": date_time,
        "done": False
    }
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.\n")
        return
    
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "DONE" if task["done"] else "NOT DONE"
        print(f"{idx}- {task['title']} - {task['date_time']} - {status}")
    print()

def mark_task_done():
    tasks = load_tasks()
    list_tasks()
    if not tasks:
        return
    
    try:
        num = int(input("Enter the task number to mark as DONE: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as DONE!\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")

def search_task():
    tasks = load_tasks()
    keyword = input("Enter keyword to search in titles: ").lower()
    results = [task for task in tasks if keyword in task["title"].lower()]
    
    if not results:
        print("No tasks found with that keyword.\n")
        return
    
    print("\nSearch Results:")
    for idx, task in enumerate(results, start=1):
        status = "DONE" if task["done"] else "NOT DONE"
        print(f"{idx}- {task['title']} - {task['date_time']} - {status}")
    print()

def main():
    while True:
        print("=== To-Do Program ===")
        print("1- Add new task")
        print("2- List tasks")
        print("3- Mark task as DONE")
        print("4- Search task")
        print("5- Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            search_task()
        elif choice == "5":
            print("Thank you for using the To-Do program, come back again soon!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
