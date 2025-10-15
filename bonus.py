import json
from datetime import datetime   # استورد لي 
# مع ذالك من الممكن اني اسويها داخل  loob عن طريق  while true كون الساعه شيء دائم يتحرك على نمط
file_name = "to_do.txt"

try:
    with open(file_name, "r", encoding="utf-8") as file: #"r",  للقراءه # 
        to_do_list = json.load(file)
except FileNotFoundError:
    to_do_list = []   # empty list  هنا انا جالسة اطلب منه مجموعه من النصوص يكتبها داخل الملف
to_do_list = json.load(file)


while True:
     user_name = input("Do you want to add a new To-Do item? Answer by 'y' for yes and 'n' for no or 'exit' to quit: ").lower()

     if user_name == "y":
        new_item = input("Enter the To-Do item: ")
        new_task = {
            "title": new_item,
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "done": False
        }
        to_do_list.append(new_task)
        print("Item added!")
     elif user_name == "n":
         show_list = input("Do you want to add a new To-Do item? Answer by 'y' for yes and 'n' for no or 'exit' to quit: ").lower()

         if show_list == "y":
             if not to_do_list:
                 print("your to-do list is empty. ")
             else:
                for i, item in enumerate(to_do_list, start=1):
                    status = "DONE" if item["done"] else "NOT DONE"
                    print(f"{i}- {item['title']} - {item['date_time']} - {status}")