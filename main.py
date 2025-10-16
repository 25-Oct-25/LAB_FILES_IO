
open("to_do.txt", "a").close()

while True:
    answer = input("Do you want to add a new To-Do item? (y/n or type 'exit' to quit): ").lower()

    if answer == "exit":
        print("Thank you for using the To-Do program")
        break

    elif answer == "y":
        new_item = input("Enter your new To-Do item: ")
        with open("to_do.txt", "a") as file:
            file.write(new_item + "\n")
        print("Item added successfully!\n")

    elif answer == "n":
        show = input("Do you want to list your To-Do items? (y/n): ").lower()
        if show == "y":
            with open("to_do.txt", "r") as file:
                items = file.readlines()
                if not items:
                    print("Your To-Do list is empty.\n")
                else:
                    print("\nYour To-Do List:")
                    for item in items:
                        print("-", item.strip())
                    print()
        else:
            print("Okay, nothing to show.\n")

    else:
        print("Invalid input, please answer with 'y', 'n', or 'exit'.\n")
