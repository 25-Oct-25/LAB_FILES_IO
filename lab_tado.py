

import json
tasks = []  


while True:
    print("\n1- Add task")
    print("2- Show tasks")
    print("3- Exit")

    choice = input("Choose: ")
    if choice == "1":
        title = input("Task title: ")
        date = input("Task date: ")
        task = {"title": title, "date": date, "done": False}
        tasks.append(task)

        print("Task added!")

    elif choice == "2":

        if not tasks:

            print("No tasks yet.")

        else:

            for t in tasks:
                status = "DONE" if t["done"] else "NOT DONE"
                print(f"{t['title']} - {t['date']} - {status}")


    elif choice == "3":
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)
        print("Saved and exited.")
        break
    else:
        print(" Invalid choice.")


