
i=1
while True:
    file= open("to_do.txt","a+",encoding="UTF-8")
    user_input=input("do you want to add a new To-Do item?(y/n/exit): ").lower().strip()
    if user_input=="y":
        todoItem=input("Enter your a new To-Do item: ")
        file.write(f"{i}- {todoItem}. ")
        i+=1
    elif user_input=="n":
        listItems=input("do you want to list your To-Do items?(y/n) ").lower().strip()
        if listItems=="y":

            file.seek(0)
            print(file.read())
    elif user_input=="exit":
        print("thank you for using the To-Do program, come back again soon")
        file.close()
        break
        


