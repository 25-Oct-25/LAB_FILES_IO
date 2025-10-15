import json
from datetime import datetime

FILE = "to_do.json"  # JSON file to store tasks

# Load tasks from file or return empty list if file not found
def load_tasks():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks list to JSON file
def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

# Add a new task with title, datetime, and done=False
def add_task():
    title = input("Enter task title: ")
    date_str = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
    try:
        datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date format! Task not added.")
        return
    task = {"title": title, "datetime": date_str, "done": False}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added!")

# List all tasks with DONE/NOT DONE status
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "DONE" if task["done"] else "NOT DONE"
        print(f"{idx}- {task['title']} - {task['datetime']} - {status}")

# Mark a specific task as done
def mark_done():
    list_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to mark as DONE: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[num-1]['title']}' marked as DONE!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Search tasks by keyword in title
def search_task():
    keyword = input("Enter a keyword to search in task titles: ").lower()
    tasks = load_tasks()
    found = False
    for idx, task in enumerate(tasks, 1):
        if keyword in task["title"].lower():
            status = "DONE" if task["done"] else "NOT DONE"
            print(f"{idx}- {task['title']} - {task['datetime']} - {status}")
            found = True
    if not found:
        print("No tasks found with that keyword.")

# Main loop for user interaction
while True:
    print("\nOptions: add, list, done, search, exit")
    choice = input("Choose an action: ").lower()
    if choice == "exit":
        print("Thank you for using the To-Do program, come back again soon!")
        break
    elif choice == "add":
        add_task()
    elif choice == "list":
        list_tasks()
    elif choice == "done":
        mark_done()
    elif choice == "search":
        search_task()
    else:
        print("Invalid option. Please choose again.")

import json
from datetime import datetime

FILE = "to_do.json"  # JSON file to store tasks

# Load tasks from file or return empty list if file not found
def load_tasks():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks list to JSON file
def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

# Add a new task with title, datetime, and done=False
def add_task():
    title = input("Enter task title: ")
    date_str = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
    try:
        datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date format! Task not added.")
        return
    task = {"title": title, "datetime": date_str, "done": False}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added!")

# List all tasks with DONE/NOT DONE status
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "DONE" if task["done"] else "NOT DONE"
        print(f"{idx}- {task['title']} - {task['datetime']} - {status}")

# Mark a specific task as done
def mark_done():
    list_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to mark as DONE: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[num-1]['title']}' marked as DONE!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Search tasks by keyword in title
def search_task():
    keyword = input("Enter a keyword to search in task titles: ").lower()
    tasks = load_tasks()
    found = False
    for idx, task in enumerate(tasks, 1):
        if keyword in task["title"].lower():
            status = "DONE" if task["done"] else "NOT DONE"
            print(f"{idx}- {task['title']} - {task['datetime']} - {status}")
            found = True
    if not found:
        print("No tasks found with that keyword.")

# Main loop for user interaction
while True:
    print("\nOptions: add, list, done, search, exit")
    choice = input("Choose an action: ").lower()
    if choice == "exit":
        print("Thank you for using the To-Do program, come back again soon!")
        break
    elif choice == "add":
        add_task()
    elif choice == "list":
        list_tasks()
    elif choice == "done":
        mark_done()
    elif choice == "search":
        search_task()
    else:
        print("Invalid option. Please choose again.")

import json
from datetime import datetime

FILE = "to_do.json"  # JSON file to store tasks

# Load tasks from file or return empty list if file not found
def load_tasks():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks list to JSON file
def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

# Add a new task with title, datetime, and done=False
def add_task():
    title = input("Enter task title: ")
    date_str = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
    try:
        datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date format! Task not added.")
        return
    task = {"title": title, "datetime": date_str, "done": False}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added!")

# List all tasks with DONE/NOT DONE status
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "DONE" if task["done"] else "NOT DONE"
        print(f"{idx}- {task['title']} - {task['datetime']} - {status}")

# Mark a specific task as done
def mark_done():
    list_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to mark as DONE: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[num-1]['title']}' marked as DONE!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Search tasks by keyword in title
def search_task():
    keyword = input("Enter a keyword to search in task titles: ").lower()
    tasks = load_tasks()
    found = False
    for idx, task in enumerate(tasks, 1):
        if keyword in task["title"].lower():
            status = "DONE" if task["done"] else "NOT DONE"
            print(f"{idx}- {task['title']} - {task['datetime']} - {status}")
            found = True
    if not found:
        print("No tasks found with that keyword.")

# Main loop for user interaction
while True:
    print("\nOptions: add, list, done, search, exit")
    choice = input("Choose an action: ").lower()
    if choice == "exit":
        print("Thank you for using the To-Do program, come back again soon!")
        break
    elif choice == "add":
        add_task()
    elif choice == "list":
        list_tasks()
    elif choice == "done":
        mark_done()
    elif choice == "search":
        search_task()
    else:
        print("Invalid option. Please choose again.")

#Features added by me:
# - Save tasks in JSON for structured storage
# - Store title, datetime, and done status for each task
# - Display tasks with DONE/NOT DONE status
# - Allow user to mark task as done
# - Search tasks by title keyword
# - Program keeps running until user types "exit"