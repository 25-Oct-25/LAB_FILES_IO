# Bonus
import json
from datetime import datetime

while True:
    user_choice  = input('Do you want to add (a), list (l), mark as done (m), search (s), or exit: ').lower()

    if user_choice  == "exit":
        print("Thank you for using the To-Do program, come back again soon!")
        break

  
    elif user_choice  == "a":
        title = input("Please type in your To-Do item: ")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open("to_do.json", "r", encoding="utf-8") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = [] 

        tasks.append({
            "title": title,
            "datetime": now,
            "done": False
        })

        with open("to_do.json", "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)

        print(f'Task "{title}" added!\n')

   
    elif user_choice  == "l":
        try:
            with open("to_do.json", "r", encoding="utf-8") as file:
                tasks = json.load(file)

            if not tasks:
                print("No To-Do items found.")
            else:
                print("\nYour To-Do List:")
                for i, task in enumerate(tasks, start=1):
                    status = "DONE" if task["done"] else "NOT DONE"
                    print(f"{i}- {task['title']} - {task['datetime']} - {status}")
                print()

        except FileNotFoundError:
            print("No To-Do file found yet! Try adding something first.\n")

       

   
    elif user_choice  == "m":
        task_num = int(input("Enter the task number you finished: "))

        with open("to_do.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)

        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True

            with open("to_do.json", "w", encoding="utf-8") as file:
                json.dump(tasks, file, indent=4)

            print(f'Task "{tasks[task_num - 1]["title"]}" marked as DONE!\n')
        else:
            print("Invalid task number.\n")

   
    elif user_choice  == "s":
        search = input("Enter part of the task title to search: ").lower()

        with open("to_do.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)

        found = False
        for i, task in enumerate(tasks, start=1):
            if search in task["title"].lower():
                status = "DONE" if task["done"] else "NOT DONE"
                print(f"{i}- {task['title']} - {task['datetime']} - {status}")
                found = True

        if not found:
            print("No matching tasks found.\n")

    else:
        print("Invalid input. Please type y, n, m, s, or exit.\n")
