import os 


while True:
    new_note = input("Do you want to add a new To-Do item? (y/n or exit): ").lower()
    
    if new_note== "exit":
        print("Thank you new To-DO program, come back again soon! ")
        break

    elif new_note == "y":
        item = input("Type your new To-Do item: ")
        with open("to-do.txt", "a", encoding="utf-8") as file:
             file.write(item +  "\n")
        print("Task added successfuly!\n")

    elif new_note == "n":
        see_list = input("Do you want to list your To-Do items? (y/n): ").lower()
        if see_list() == "y":
            if so.path.exists("to_do.txt"):
                with open("to_do.txt", "r", encoding="utf-8") as file:
                  content = file.read()
                  print("\nYour To-Do List: ")
                  print(content if content.strip() else "No tasks found yet!\n")
                  print("-------------------------\n")
        else:
            print("No task found yet\n")
    else:
        print("Okay, nothing to show.\n")
else:
    print("Please enter only y, n, or exit. \n")