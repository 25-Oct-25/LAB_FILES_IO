
def toDoList():
     while True:
        q1 = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no. ")

        if q1 == 'exit':
            print("thank you for using the To-Do program, come back again soon")
            break   


        elif q1 == 'y':
            
            while True:
                file = open("to_do.txt", "a+", encoding="UTF-8")
                user_note = input("type your to do item: ")
                file.write(user_note + "\n")
                if user_note == "exit":
                    print("thank you for using the To-Do program, come back again soon")
                    break

        elif q1 == 'n':
            q2 = input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no. ")

            if q2 == 'exit':
                print("thank you for using the To-Do program, come back again soon")
                break

            if q2 == 'y':
                file = open("to_do.txt", "r", encoding="utf-8")
                content = file.read()
                print(content)
                file.close()
            
            elif q2 == 'n':
                print("thank you for using the To-Do program, come back again soon")
                break


toDoList()