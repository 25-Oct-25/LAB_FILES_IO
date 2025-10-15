# To-Do List program using basic File I/O

FILENAME = "to_do.txt"

# 1) تأكيد وجود الملف (إنشاء ملف فاضي إذا ما كان موجود)
# نفتح للإلحاق ونغلق فورًا؛ هذا ينشئه إن لم يوجد.
open(FILENAME, "a").close()


# First question loop
while True:
    choice = input('Do you want to add a new To-Do item? (y/n) or type "exit": ').strip().lower()
    #check for exit
    if choice == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break
    # check for yes
    if choice == "y":
        item = input("Type your new To-Do item: ").strip()
        if item:  # نتأكد مو فاضي
            with open(FILENAME, "a", encoding="utf-8") as f:
                f.write(item + "\n")
         
        continue
    # check for no
    if choice == "n":
       
        see_list = input('Do you want to list your To-Do items? (y/n): ').strip().lower()
        if see_list == "y":
           
            with open(FILENAME, "r", encoding="utf-8") as f:
                lines = [line.rstrip("\n") for line in f]
            if lines:
                print("\nYour To-Do list:")
                for task in lines:
                    print(task)
                print()   
            else:
                print("Your To-Do list is empty.\n")
      
        continue

    
    print('Please enter "y", "n", or "exit".')
