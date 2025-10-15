
# to_do.py


print("Welcome to the To-Do List program!")
while True:
    user_choice = input("\nDo you want to add a new To-Do item? (y/n or type 'exit' to quit): ").strip().lower()

    if user_choice == "exit":
        print("\nThank you for using the To-Do program, come back again soon!")
        break

    elif user_choice == "y":
        todo_item = input("Enter your new To-Do item: ").strip()
        
        with open("to_do.txt", "a") as file:
            file.write(todo_item + "\n")
        print(f"'{todo_item}' added to your To-Do list.")

    elif user_choice == "n":
        list_choice = input("Do you want to list your To-Do items? (y/n): ").strip().lower()
        if list_choice == "y":
            try:
                with open("to_do.txt", "r") as file:
                    todos = file.readlines()
                if todos:
                    print("\n📝 Your To-Do List:")
                    for index, item in enumerate(todos, start=1):
                        print(f"{index}. {item.strip()}")
                else:
                    print("Your To-Do list is empty!")
            except FileNotFoundError:
                print("You don't have a To-Do list yet. Add something first!")
        elif list_choice == "n":
            continue
        else:
            print("Invalid input. Please type 'y' or 'n'.")
    else:
        print("Invalid input. Please type 'y', 'n', or 'exit'.")