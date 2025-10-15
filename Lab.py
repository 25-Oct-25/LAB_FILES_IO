file= open("to_do.txt","w", encoding="utf-8")

while True:
    service= input("Do you want to add a new To-Do item?\n (Enter 'y' for Yes of 'n' for No)\n")


    if service=="exit":
        print("Thank you for using the To-Do list program, com back again soon!")
        break

    elif service=="y":
        to_do_item= input("Please write your new item:\n")

        file= open("to_do.txt","a", encoding="utf-8")
        file.write(to_do_item +"\n")
        file.close()

    elif service=="n":
        read=input("Do you want to disply your To-Do items?\n (Enter 'y' for Yes of 'n' for No)\n")

        if read=="y":
            file = open("to_do.txt","r", encoding="utf-8")
            print("Your To-Do list is:\n\n")
            file.seek(0)
            print(file.read())
            file.close()