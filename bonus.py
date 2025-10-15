import json
from datetime import datetime

def load_todos(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_todos(filename, todos):
    with open(filename, "w") as file:
        json.dump(todos, file, indent=4)

def display_todos(todos):
    if not todos:
        print("Your To-Do list is empty.")
        return
    for index, todo in enumerate(todos, start=1):
        status = "DONE" if todo['done'] else "NOT DONE"
        print(f"{index}- {todo['title']} - {todo['date']} - {status}")

def mark_done(todos):
    title = input("Enter the title of the To-Do item to mark as done: ").strip()
    for todo in todos:
        if todo['title'].lower() == title.lower():
            todo['done'] = True
            print(f'To-Do item "{title}" marked as DONE.')
            return
    print("To-Do item not found.")

def search_todos(todos):
    title = input("Enter the title to search for: ").strip()
    found = [todo for todo in todos if title.lower() in todo['title'].lower()]
    
    if found:
        print("Search results:")
        display_todos(found)
    else:
        print("No matching To-Do items found.")

def main():
    filename = "to_do.json"
    todos = load_todos(filename)

    while True:
        user_input = input("Do you want to add a new To-Do item? (y/n or type 'exit' to quit): ").strip().lower()

        if user_input == 'exit':
            save_todos(filename, todos)
            print("Thank you for using the To-Do program, come back again soon!")
            break
        
        if user_input == 'y':
            title = input("Please type in your new To-Do item: ").strip()
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            todos.append({"title": title, "date": date_time, "done": False})
            print(f'To-Do item "{title}" added!')

        elif user_input == 'n':
            action = input("What would you like to do? (list/mark/search): ").strip().lower()
            if action == 'list':
                display_todos(todos)
            elif action == 'mark':
                mark_done(todos)
            elif action == 'search':
                search_todos(todos)
            else:
                print("Invalid action. Please enter 'list', 'mark', or 'search'.")
        
        else:
            print("Invalid input. Please enter 'y', 'n', or 'exit'.")

if __name__ == "__main__":
    main()