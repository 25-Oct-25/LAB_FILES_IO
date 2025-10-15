import json
from datetime import datetime


FILE_NAME = "to_do.json"


def load_tasks():
    '''load tasks from the file'''
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # If the file empty or not fond



def save_tasks(tasks):
    '''save tasks in the file'''
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)



def add_task():
    '''load and save what the user write'''
    title = input("Enter your To-Do title: ").strip()
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")# add the date when the user wrote it 
    new_task = {"title": title, "date_time": date_time, "done": False}

    tasks = load_tasks()
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"'{title}' added successfully!")



def list_tasks():
    '''list all tasks by every one item per line.'''
    tasks = load_tasks()
    if not tasks:
        print("📭 Your To-Do list is empty.")
        return

    print("\n📝 Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "DONE" if task["done"] else "NOT DONE"
        print(f"{i}- {task['title']} - {task['date_time']} - {status}")



def mark_done():
    '''mark the tasks if is done or not'''
    tasks = load_tasks()
    list_tasks()
    if not tasks:
        return

    try:
        num = int(input("\nEnter the task number you want to mark as DONE: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"'{tasks[num - 1]['title']}' marked as DONE!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")



def search_task():
    '''search a task in the file '''
    tasks = load_tasks()
    query = input("Enter a keyword to search in your tasks: ").strip().lower()

    found = [t for t in tasks if query in t["title"].lower()]
    if found:
        print("\n🔍 Search Results:")
        for i, task in enumerate(found, start=1):
            status = "DONE" if task["done"] else "NOT DONE"
            print(f"{i}- {task['title']} - {task['date_time']} - {status}")
    else:
        print("No tasks found with that title.")



def main():
    print("👋 Welcome to the To-Do List JSON Program!")

    while True:
        print("\nMenu:")
        print("1. Add new To-Do")
        print("2. List all To-Dos")
        print("3. Mark task as DONE")
        print("4. Search task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            search_task()
        elif choice == "5":
            print("\nThank you for using the To-Do program, come back again soon! 👋")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
