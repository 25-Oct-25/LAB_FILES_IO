while True:
    print("\nYou want to add a new To-Do item?")
    print("1 - Yes")
    print("2 - No")
    print("3 - Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        new_item = input("Type your new To-Do item: ")

        with open("to_do.txt", "a") as file:
            file.write(new_item + "\n")

        print("Your To-Do item has been added successfully!")

    elif choice == "2":
        print("\nDo you want to list your To-Do items?")
        print("1 - Yes")
        print("2 - No")

        list_choice = input("Enter your choice (1/2): ")

        if list_choice == "1":
            try:
                with open("to_do.txt", "r") as file:
                    tasks = file.readlines()

                    if len(tasks) == 0:
                        print("Your To-Do list is empty.")
                    else:
                        print("\nYour To-Do items:")
                        for i, task in enumerate(tasks, start=1):
                            print(f"{i}. {task.strip()}")

            except FileNotFoundError:
                print("No To-Do list found yet. Add a task first!")

        elif list_choice == "2":
            print("Okay, returning to main menu...")

        else:
            print("Invalid choice, please try again.")

    elif choice == "3":
        print("Thank you for using the To-Do program, come back again soon!")
        break

    else:
        print("Invalid choice, please enter 1, 2, or 3.")

