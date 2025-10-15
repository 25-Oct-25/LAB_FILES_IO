# To-Do List Program
while True:
    choice = input("Add new To-Do? (y/n) or 'exit' to quit: ").lower()
    if choice == "exit":
        print("Thank you for using the To-Do program, come back again soon!")
        break
    elif choice == "y":
        item = input("Enter new To-Do item: ")
        with open("to_do.txt", "a", encoding="utf-8") as f:
            f.write(item + "\n")
        print(f"'{item}' added!")
    elif choice == "n":
        list_choice = input("List your To-Do items? (y/n): ").lower()
        if list_choice == "y":
            try:
                with open("to_do.txt", "r", encoding="utf-8") as f:
                    for idx, line in enumerate(f, 1):
                        print(f"{idx}. {line.strip()}")
            except FileNotFoundError:
                print("No To-Do items yet.")
