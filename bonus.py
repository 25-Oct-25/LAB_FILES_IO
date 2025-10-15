import json
from datetime import datetime

try:
    with open("to_do.json", "r") as f:
        todos = json.load(f)
except:
    todos = []

while True:
    choice = input("1-Add 2-List 3-Mark Done 4-Search 5-Exit: ")
    if choice == "1":
        title = input("Enter title: ")
        todos.append({"title": title, "date": str(datetime.now()), "done": False})
        with open("to_do.json", "w") as f:
            json.dump(todos, f)
    elif choice == "2":
        for i, t in enumerate(todos, 1):
            status = "DONE" if t["done"] else "NOT DONE"
            print(f"{i}- {t['title']} - {t['date']} - {status}")
    elif choice == "3":
        num = int(input("Enter task number to mark done: "))
        if 0 < num <= len(todos):
            todos[num-1]["done"] = True
            with open("to_do.json", "w") as f:
                json.dump(todos, f)
    elif choice == "4":
        word = input("Enter title to search: ")
        for t in todos:
            if word.lower() in t["title"].lower():
                status = "DONE" if t["done"] else "NOT DONE"
                print(f"{t['title']} - {t['date']} - {status}")
    elif choice == "5":
        print("thank you for using the To-Do program, come back again soon")
        break
