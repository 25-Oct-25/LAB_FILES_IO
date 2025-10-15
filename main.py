import os


with open("to_do.txt", "w", encoding="UTF-8") as file:
    file.write("my list note\n")  

# read it 
with open("to_do.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# start the loob for yes and no 
while True:
    user_name = input("Do you want to add a new To-Do item? Answer by 'y' for yes and 'n' for no: ").lower()
    
    if user_name == "y":
        new_item = input("Enter the To-Do item: ")
        with open("to_do.txt", "a", encoding="UTF-8") as file:
            file.write(new_item + "\n")
        print("Item added!")
        
    elif user_name == "n":
        print("Exiting the program.")
        break  # stoop the loob
        
    else:
        print("Please enter 'y' or 'n'.")


