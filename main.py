while True:
    choice = input("Do you want to add a new To-Do item? (y/n or type 'exit' to quit): ")

    if choice.lower() == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break

    if choice.lower() == "y":
        item = input("Type in your new To-Do item: ")
        with open("to_do.txt", "a") as file:   
            file.write(item + "\n")
        print("Item added successfully!\n")

    elif choice.lower() == "n":
        list_choice = input("Do you want to list your To-Do items? (y/n): ")
        
        if list_choice.lower() == "y":
            try:
                with open("to_do.txt", "r") as file:
                    todos = file.readlines()
                    print("\nYour To-Do List:")
                    for idx, todo in enumerate(todos, start=1):
                        print(f"{idx}. {todo.strip()}")
                    print()
            except FileNotFoundError:
                print("Your To-Do list is empty (no file found).\n")
        elif list_choice.lower() == "n":
            print("Okay, nothing to do now.\n")

    else:
        print("Invalid choice, please type 'y', 'n', or 'exit'.\n")
