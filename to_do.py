# LAB_FILES_IO
while True:
    add_item = input('Do you want to add a new To-Do item? (y/n or type "exit" to quit): ').lower()

    if add_item == "exit":
        print("Thank you for using the To-Do program, come back again soon!")
        break

    elif add_item == "y":
        type_item = input("Please type in your To-Do item: ")
         # open the file to add the new task 
        with open("to_do.txt", "a", encoding="utf-8") as file:
            file.write(type_item + "\n") # add new line after the item 
        print(f'Added: "{type_item}"\n')

    elif add_item == "n":
        list_item = input('Do you want to list your To-Do items? (y/n): ').lower()
        if list_item == "y":
            try:
                # open file and read all lines
                with open("to_do.txt", "r", encoding="utf-8") as read_file:
                    content = read_file.readlines() # read all lines from file
                    print("\nA list of the To-Do items:")
                    # print every task in one line
                    for item in content:
                        print(item.strip())
                    print()
            except FileNotFoundError:
                print("No To-Do list found. Try adding an item first!\n")

        elif list_item == "n":
            print("Okay, returning to main menu.\n")
        else:
            print("Invalid input. Please type y or n.\n")

    else:
        print("Invalid input. Please type y, n, or exit.\n")


    

    


