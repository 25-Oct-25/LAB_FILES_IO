import json
import os

FILENAME = "To-Do.json"

def set_done_by_title(title, done=False):
    with open(FILENAME, "r", encoding="utf-8") as f:
        tasks = json.load(f)  # list[dict]

    # find the first title match (case-insensitive, trims spaces)
    norm = title.strip().casefold()
    updated = False
    for t in tasks:
        if t.get("title", "").strip().casefold() == norm:
            t["done"] = done
            updated = True
            break

    if not updated:
        print(f"Task with title '{title}' not found.")
        return

    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)
    print(f"Updated '{title}' → {'DONE' if done else 'NOT DONE'}")

# Ensure file exists and is a JSON list
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)

while True:
    user_input = input("do you want to add a new To-Do item?(y/n/exit): ").lower().strip()

    if user_input == "y":
        title = input("Enter your new To-Do title: ").strip()
        datetime_str = input("Enter date & time (e.g., 02-02-2022 00:02:02): ").strip()
        task = {
            "title": title,
            "datetime": datetime_str,
            "done": False
        }

        
        with open(FILENAME, "r+", encoding="utf-8") as file:
            try:
                data = json.load(file)  
            except json.JSONDecodeError:
                data = []
            data.append(task)
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
            file.truncate()

    elif user_input == "n":
        listItems = input("do you want to list your To-Do items?(y/n) ").lower().strip()
        if listItems == "y":
            with open(FILENAME, "r", encoding="utf-8") as file:
                try:
                    file.seek(0)
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
            if not data:
                print("(no items yet)")
            else:
                for i, item in enumerate(data, start=1):
                    status = "DONE" if item.get("done") else "NOT DONE"
                    print(f"{i}- {item.get('title','')} - {item.get('datetime','')} - {status}")
        elif listItems == "n":
            chstatus = input("Are you done the task?(y/n) ").lower().strip()
            if chstatus == "y":
                title = input("Enter your To-Do title that want to chagne the state to done: ").strip()
                done=True
                set_done_by_title(title,done)
                  
                  
    elif user_input == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break
