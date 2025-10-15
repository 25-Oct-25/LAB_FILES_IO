import json
from datetime import datetime

file_name = "to_do.json"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        todos = json.load(file)
except FileNotFoundError:
    todos = []

print("Welcome to the To-Do program (JSON Version)!\n")
  # Display the main menu options
while True:
    print("Options:")
    print("1. Add new task 🖊️ :")
    print("2. Show all tasks 📝 :")
    print("3. Mark a task as Done ✅:")
    print("4. Search for a task by title 🔍:")
    print("5. Exit 🏃:")

    choice = input("Choose (1-5): ").strip()

    if choice == "1":
       # Add a new task
        title = input("Enter task title: ").strip()
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        todo = {"title": title, "date_time": date_time, "done": False}
        todos.append(todo)

        # Save the file
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(todos, file, indent=4)
        print(f"'{title}' added successfully!\n")

    elif choice == "2":
        # Show all tasks
        if not todos:
            print("Your list is empty 📭.\n")
        else:
            print("\nYour List:")
            for i, todo in enumerate(todos, 1):
                status = "DONE" if todo["done"] else "NOT DONE"
                print(f"{i}- {todo['title']} - {todo['date_time']} - {status}")
            print()

    elif choice == "3":
       # Mark a task as done
        if not todos:
            print("No tasks to mark as done.\n")
        else:
            for i, todo in enumerate(todos, 1):
                status = "DONE" if todo["done"] else "NOT DONE"
                print(f"{i}- {todo['title']} - {status}")

            num = input("Enter task number to mark as done: ").strip()
            if num.isdigit() and 1 <= int(num) <= len(todos):
                todos[int(num) - 1]["done"] = True
                with open(file_name, "w", encoding="utf-8") as file:
                    json.dump(todos, file, indent=4)
                print(f"Task '{todos[int(num)-1]['title']}' marked as DONE!\n")
            else:
                print("Invalid number .\n")

    elif choice == "4":
        # البحث في المهام
        search_title = input("Enter title to search: ").strip().lower()
        found = False
        for todo in todos:
            if search_title in todo["title"].lower():
                status = "DONE" if todo["done"] else "NOT DONE"
                print(f"- {todo['title']} - {todo['date_time']} - {status}")
                found = True
        if not found:
            print("No matching tasks found.\n")
        print()

    elif choice == "5":
        print(" Well done! Thanks for using the program!🏆")
        break
    
 # Invalid menu option
    else:
        print("Invalid choice❗Please enter 1–5.\n")
