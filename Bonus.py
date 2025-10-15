import json

file="to_do.json"

def write_data(data,file):
    with open (file,"w",encoding="utf-8") as task:
        json.dump(data,task, indent=4)
        print(f"New To-Do file was created successfuly.")


to_do_items={}


while True:

    menu= '''
    1- Add
    2- Print
    3- Done
    4- Serch
    5- Exit
'''

    print(menu)

    service= int (input("What do you wish to do?\n"))

    if service==1:

        title= input("Please type the name of the task:\n")
        date_time= input("Please type the date and the time of the item:\n")

        new_item={

            "Title":title,
            "Date & Time":date_time,
            "Status": False
        }
        to_do_items[title]= new_item

        write_data(to_do_items,file)

    elif service==2:

        with open(file,"r", encoding="utf-8") as json_file:
            tasks= json.load(json_file)

        for num, data in enumerate(tasks, start=1):

            if tasks[data]["Status"]==True:
                status= "DONE"
            else:
                status= "NOT DONE"

                print(f"{num}- {data} - {tasks[title]["Date & Time"]} - {status}")
    
    elif service==3:
        with open(file,"r", encoding="utf-8") as json_file:
            tasks= json.load(json_file)

        for data in tasks.values():
            if tasks[title]["Status"]==True:
                status= "DONE"
            else:
                status= "NOT DONE"

        done=input("Please type the title of the task you want to mark as DONE:\n")

        if done in tasks:
            if tasks[done]["Status"] ==True:
                print(f"Task {done} is already marked as DONE.")
            elif tasks[done]["Status"] ==False:
                
                tasks[done]["Status"] =True
                print("task marked as done successfuly.")
        else:
            print(f"Sorry {title} not found.")

    elif service==4:
        with open(file,"r", encoding="utf-8") as json_file:
            tasks= json.load(json_file)

        search=input("Please enter the title of the item:\n")
        if search in tasks:
            for data in tasks.values():
                if tasks[title]["Status"]==True:
                    status= "DONE"
                else:
                    status= "NOT DONE"

                print(f"{title} - {tasks[title]["Date & Time"]} - {status}")
        else:
            print(f"Sorry {title} not found")


    elif service== 5:
        print("Thank you ")
        break