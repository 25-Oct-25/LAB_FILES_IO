import os

file_name = "to_do.txt"

print("Let's organize your day! 📝\n")

while True:
    choice = input("Do you want to add a new task? (y/n) or 'exit': ").strip().lower()

    if choice == "exit":
        print("Thank you for using the To-Do List! Come back soon! 👋")
        break

    elif choice == "y":
        item = input("Add new task 🖊️: ").strip()
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(item + "\n")
        print(f"'{item}' added!\n")

    elif choice == "n":
        list_choice = input("Do you want to see your tasks 👀? (y/n): ").strip().lower()
        if list_choice == "y":
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    for line in f:
                        print(line.strip())  # عرض المهام
            except FileNotFoundError:
                print("Your list is empty.")
        print()  # سطر فارغ للوضوح

    else:
        print("Invalid input❗Please type 'y', 'n', or 'exit'.\n")
