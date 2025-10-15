import json
from datetime import date
import time

class To_Do:

    #Create class attributes
    def __init__(self, title:str,task_date:date, task_time:time, done:bool):
        self.title = title
        self.task_date = task_date
        self.task_time = task_time
        self.done = False
    
        #Create add task method
    """    def add_task (self, task_title:str, task_date:date, task_time:time, done:bool ):
            file"""
    pass
    
project1 = To_Do("",date.today,time.time,False)
done = project1.done

i = 1
while True:
    user_input = input("Do you want add a new item? type 'y' for yes, and 'n' for no")
    if user_input == 'y':
        project1.title = input("Enter your task title ")
        project1.task_date = input("Enter your task date (year , month, day) ")
        project1.task_time = input("Enter your task time (hour,mintus,seconds)")

        #Create a file to write task on it
        file = open('to_do.txt', 'a+', encoding="UTF-8")
        file.write('\n',i ,'- ',project1.title, ' - ',project1.task_date, " ", project1.task_time,' - ' )
        if done == False:
            print("NOT DONE")
        else: print ("DONE")
        file.close()
    elif user_input == 'n':
        user_input= input("Do you want to list your To-Do items ? type 'y' for yes and 'n' for no")
        if user_input == 'y':
            file = open("to_do.txt", 'r', encoding="UTF-8")
            file.seek(0)
            print(file.readline())
    user_input = input("To  exit you can write 'exit', or press 'enter' to countinue")
    if (user_input == 'exit'):
        break
print('Thank you for using To-Do program, come back again soon')
