import time
import json

file_path = "Lab11/Bouns/To_Do.json"

def to_do_list():
    
    to_do = ("""
    ========= To Do =========
    1. Add Task
    2. Edit Task
    3. Show User Tasks
    4. Show All Tasks
    5. Search Task
    6. Exit
    """)

    while True:

        print(to_do)
        
        choice = input("Enter a number: ")

        if choice == "1":
            
            name = input("Enter your name: ")
            title = input("Enter task title: ")
            date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            done = input("Did you complete the task? (yes/no): ")

            if done.lower() == "yes" or done.lower() == "y":
                done_status = True
            else:
                done_status = False

            add_task(name, title, date_time, done_status)

        elif choice == "2":
            name = input("Enter your name: ")
            title = input("Enter the task title you want to edit: ")
            date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            done = input("Did you complete the task? (yes/no): ")

            if done.lower() == "yes" or done.lower() == "y":
                done_status = True
            else:
                done_status = False

            edit_task(name, title, date_time, done_status)

        elif choice == "3":
            name = input("Enter your name: ")
            show_user_tasks(name)

        elif choice == "4":
            show_all_tasks()

        elif choice == "5":
            title = input("Enter title to search: ")
            search_task(title)

        elif choice == "6":
            print("Thank you for using the To-Do program!")
            break

        else:
            print("Invalid choice! Please try again.")


def add_task(name, title, date_time, done):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    new_task = {
        "user_name": name,
        "task_title": title,
        "date_time": date_time,
        "done": done
    }

    tasks.append(new_task)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

    print("Task added successfully!\n")


def edit_task(name, title, date_time, done):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("File not found!")
        return

    found = False
    for task in tasks:
        if task["user_name"] == name and task["task_title"] == title:
            task["date_time"] = date_time
            task["done"] = done
            found = True
            break

    if found:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        print("Task updated successfully!\n")
    else:
        print("Task not found!\n")


def show_all_tasks():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("File not found!")
        return

    if not tasks:
        print("No tasks found!\n")
        return

    print("\n========= All Tasks =========")
    for task in tasks:
        if task["done"]:
            status = "DONE"
        else:
            status = "NOT DONE"

        print(f"Name: {task['user_name']} | Task: {task['task_title']} | Date: {task['date_time']} | Status: {status}")
    print("=============================\n")


def show_user_tasks(name):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("File not found!")
        return

    found = False
    for task in tasks:
        if task["user_name"].lower() == name.lower():
            found = True
            if task["done"]:
                status = "DONE"
            else:
                status = "NOT DONE"
            print(f"Task: {task['task_title']} | Date: {task['date_time']} | Status: {status}")

    if not found:
        print(f"No tasks found for {name}.\n")


def search_task(title):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("File not found!")
        return

    found = False
    for task in tasks:
        if title.lower() in task["task_title"].lower():
            found = True
            if task["done"]:
                status = "DONE"
            else:
                status = "NOT DONE"
            print(f"Name: {task['user_name']} | Task: {task['task_title']} | Date: {task['date_time']} | Status: {status}")

    if not found:
        print("No matching tasks found.\n")



# Call the main function :
to_do_list()