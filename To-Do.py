def main():
    while True:
        user_input = input("Do you want to add a new To-Do item? (y/n or type 'exit' to quit): ").strip().lower()

        if user_input == 'exit':
            print("Thank you for using the To-Do program, come back again soon!")
            break
        
        if user_input == 'y':
            new_todo = input("Please type in your new To-Do item: ").strip()
            with open("to_do.txt", "a") as file:
                file.write(new_todo + "\n")
            print(f'To-Do item "{new_todo}" added!')

        elif user_input == 'n':
            list_input = input("Do you want to list your To-Do items? (y/n): ").strip().lower()
            if list_input == 'y':
                try:
                    with open("to_do.txt", "r") as file:
                        todos = file.readlines()
                        if todos:
                            print("Your To-Do items:")
                            for item in todos:
                                print(f"- {item.strip()}")
                        else:
                            print("Your To-Do list is empty.")
                except FileNotFoundError:
                    print("No To-Do items found. Please add some first.")
        
        else:
            print("Invalid input. Please enter 'y', 'n', or 'exit'.")

if __name__ == "__main__":
    main()