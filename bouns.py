import json
from datetime import datetime

def load_tasks():
    try:
        with open("to_do.json","r",encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open("to_do.json","w",encoding="UTF-8") as file:
        json.dump(tasks,file,indent=4)

tasks=load_tasks()


while True:
    user_input_add = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no. or exit to quit. ").lower()
    if user_input_add == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break
    elif user_input_add == "y":
        title = input("Enter title of the task: ")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks.append({"title": title, "date & time": current_time, "done": False})
        save_tasks(tasks)
        print("the task added successfully")
    elif user_input_add == "n":
        user_input_list = input("do you want to list your To-Do items? answer 'y' for yes and 'n' for no. ").lower()
        if user_input_list == "y":
            for i, task in enumerate(tasks):
                status = "DONE" if task["done"] else "NOT DONE"
                print(f"{i+1}. {task['title']} - {task['date & time']} - {status}")
        user_input_mark = input("do you want to put the task as done? answer 'y' for yes and 'n' for no. ").lower()
        if user_input_mark == "y":
            search_title = input("Please enter the title of the task: ").lower()
            found = False
            for task in tasks:
                if task["title"].lower() == search_title:
                    task["done"] = True
                    save_tasks(tasks)
                    print("Updated the status of task successfully")
                    found = True
                    break
            if not found:
                print("does not find the task you entered")
        user_input_search = input("do you want to search for task by the title? answer 'y' for yes and 'n' for no").lower()
        if user_input_search == "y":
            search_term = input("Enter the title: ").lower()
            found = [task for task in tasks if search_term in task["title"].lower()]
            if found:
                for task in found:
                    status = "DONE" if task["done"] else "NOT DONE"
                    print(f"{task['title']} - {task['date & time']} - {status}")
            else:
                print("No tasks found matching the search term")
    else:
        print("invalid input, please try again")