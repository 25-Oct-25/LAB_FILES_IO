import json
from datetime import datetime
import os

def toDoList():
    while True:
        q1 = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no. ")

        if q1 == 'exit':
            print("thank you for using the To-Do program, come back again soon")
            break   

        elif q1 == 'y':
            while True:
            
                file = open("to_do.json", "r", encoding="UTF-8")
                tasks = json.load(file)
                user_note = input("type your to do item: ")

                if user_note == "exit":
                    print("thank you for using the To-Do program, come back again soon")
                    break

                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                task = {"title": user_note, "datetime": now, "done": False}
                tasks.append(task)

                file = open("to_do.json", "w", encoding="UTF-8")
                json.dump(tasks, file, ensure_ascii=False, indent=4)
                file.close()

        elif q1 == 'n':
            q2 = input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no. ")

            if q2 == 'exit':
                print("thank you for using the To-Do program, come back again soon")
                break

            if q2 == 'y':
                
                    file = open("to_do.json", "r", encoding="UTF-8")
                    tasks = json.load(file)

                    for i, task in enumerate(tasks, start=1):
                        status = "DONE" if task["done"] else "NOT DONE"
                        print(f"{i}- {task['title']} - {task['datetime']} - {status}")

                    done_q = input("Do you want to mark a task as done? answer 'y' for yes and 'n' for no: ")
                    if done_q == 'y':
                        num = int(input("Enter task number: "))
                        if 1 <= num <= len(tasks):
                            tasks[num-1]["done"] = True
                            file = open("to_do.json", "w", encoding="UTF-8")
                            json.dump(tasks, file, ensure_ascii=False, indent=4)
                            file.close()
                            print("Task marked as DONE.")

            elif q2 == 'n':
                print("thank you for using the To-Do program, come back again soon")
                break


toDoList()
