import json
from datetime import datetime

FILENAME = "to_do.json"

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    title = input("Enter task title: ")
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({"title": title, "date_time": date_time, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for i, t in enumerate(tasks, start=1):
        status = "DONE" if t["done"] else "NOT DONE"
        print(f"{i}- {t['title']} - {t['date_time']} - {status}")

def mark_done(tasks):
    list_tasks(tasks)
    try:
        i = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= i < len(tasks):
            tasks[i]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def search_task(tasks):
    key = input("Enter title to search: ").lower()
    found = False
    for t in tasks:
        if key in t["title"].lower():
            print(f"{t['title']} - {t['date_time']} - {'DONE' if t['done'] else 'NOT DONE'}")
            found = True
    if not found:
        print("No matching tasks found.")

tasks = load_tasks()

while True:
    print("\n1- Add Task\n2- List Tasks\n3- Mark as Done\n4- Search\n5- Exit")
    ch = input("Choose: ")

    if ch == "1":
        add_task(tasks)
    elif ch == "2":
        list_tasks(tasks)
    elif ch == "3":
        mark_done(tasks)
    elif ch == "4":
        search_task(tasks)
    elif ch == "5":
        print("Thank you for using the To-Do program, come back again soon!")
        break
    else:
        print("Invalid choice. Please try again.")
