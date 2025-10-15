
with open("to_do.txt","+a",encoding="UTF-8") as file:
    while True:
        user_input_add=input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no. or exit to quit ")

        if user_input_add.lower() == "exit":
            print("thank you for using the To-Do program, come back again soon")
            break
        elif user_input_add.lower() == "y":
            new_item=input("What item do you want to add to T0-Do ")
            with open("to_do.txt","+a",encoding="UTF-8") as file:
                file.write(new_item +'\n')
        elif user_input_add.lower() == "n":
            user_input_list=input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no ")
            if user_input_list.lower() == "y":
                with open("to_do.txt","r",encoding="UTF-8") as read_file:
                    print(read_file.read().strip())
            elif user_input_list.lower() == "n":
                continue
        else:
            print("invalid input , please try again")
