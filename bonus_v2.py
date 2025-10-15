
import json, os

FILENAME = "to_do.json"

# Ensure file exists with an empty list
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump([], f)

def load_tasks():
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def show(tasks):
    if not tasks:
        print("Your list is empty.\n"); return
    for i, t in enumerate(tasks, 1):
        status = "DONE" if t["done"] else "NOT DONE"
        print(f"{i}- {t['title']} - {t['datetime']} - {status}")
    print()

while True:
    print("1) Add  2) Show  3) Mark as Done  4) Search  5) Exit")
    c = input("Choose: ").strip()

    if c == "1":
        title = input("Title: ").strip()
        dt    = input("Date & time (any text format): ").strip()
        tasks = load_tasks()
        tasks.append({"title": title, "datetime": dt, "done": False})
        save_tasks(tasks)
        print("Added.\n")

    elif c == "2":
        show(load_tasks())

    elif c == "3":
        tasks = load_tasks()
        show(tasks)
        n = input("Task number to mark as DONE: ").strip()
        if n.isdigit():
            idx = int(n) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
                save_tasks(tasks)
                print("Marked as DONE.\n")

    elif c == "4":
        q = input("Search by title: ").strip().lower()
        tasks = load_tasks()
        results = [t for t in tasks if q in t["title"].lower()]
        show(results)

    elif c == "5":
        print("Thank you for using the To-Do program, come back again soon")
        break

    else:
        print("Invalid option.\n")
