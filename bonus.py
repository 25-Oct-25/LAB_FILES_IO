import json
import datetime
import time

#define dictionary variables
task_title =""
task_date = datetime.date(2025,10,15)
task_time = datetime.time()
done = False

#Create a list of dictionary
general_list = [{}]

#Create a to-do list has type dictionary
to_do_list = {
    'title': task_title,
    'date': task_date,
    'time' : task_time,
    'done' : done
}

i = 0

while True:
    i += 1
    #add value to variable and write to file
    print('As following instruction enter your To-Do task list:')
    task_title = input('Write now your task title: ')
    if task_title == "exit":
        break
    year = int(input('Write now your task year : '))
    month = int(input('Write now your task month : '))
    day = int(input('Write now your task day : '))
    task_date = datetime.date(year,month,day)
    done = input("Is the task done? *write False with capital F if the task not done, and write True with capital T if the task done")

    #add the data to the dictionary list
    to_do_list["title"] = task_title
    to_do_list["date"] = task_date
    to_do_list["time"] = task_time
    to_do_list["done"] = done
    general_list.append(to_do_list)

    #test
    print(f'Your task date is {task_date}')

    file = open("to-do list upgrade.txt", "a+", encoding="UTF -8")
    file.write(str(i))
    file.write("- "+ task_title + " - "+ str(task_date) + " "+str(task_time) + " - " )
    if done == 'False':
        file.write("NOT DONE \n")
    else: file.write("DONE \n")
    file.seek(0)
    print(file.readline())
    file.close()

#test
print(general_list)