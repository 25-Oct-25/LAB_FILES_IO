while True:
    choice = input("Do you want to add a new To-Do item? (y/n or exit): ")
    if choice == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break
    elif choice == "y":
        item = input("Enter your new To-Do item: ")
        with open("to_do.txt", "a") as file:
            file.write(item + "\n")
    elif choice == "n":
        show = input("Do you want to list your To-Do items? (y/n): ")
        if show == "y":
            try:
                with open("to_do.txt", "r") as file:
                    items = file.readlines()
                    for item in items:
                        print(item.strip())
            except FileNotFoundError:
                print("No To-Do list found.")
