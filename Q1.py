from datetime import datetime
now:str = datetime.now()


while True:
    user_input:str = input("do you want to add a new To-Do item? answer by 'y' for yes, 'n' for no and 'exit' for end the program: ")
    
    if user_input == "y":
        user_note = input("Type in your new To-Do item: ")
        to_do = open('to_do.txt', "a+",encoding= "utf-8")
        to_do.write(user_note + " " + str(now) + "\n")
        to_do.close()
        user_input = ""

    elif user_input == "n":
        user_input = input("do you want to list your To-Do items? answer by 'y' for yes, 'n' for no and 'exit' for end the program: ")
        
        if user_input == "y":
            to_do = open('to_do.txt', "r",encoding= "utf-8")
            content:str = to_do.read()
            to_do.close()
            print(content)

        elif user_input == "n":
            pass
        
        elif user_input == "exit":
            break
            
        else:
            print("not found")
            pass
    
    elif user_input == "exit":
        break
    else:
        print("not found")
        pass

print("thank you for using the To-Do program, come back again soon")