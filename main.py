path ="/Users/nawaf/Documents/python-camp/PY/LAB_FILES_IO/to_do.txt"

def add_item(item):
    with open (path, "a", encoding="utf-8") as file:
        file.write(item + "\n")        

def view_items():
    with open (path, "r", encoding ="utf-8") as file:
        items = file.readlines()
        for index, item in enumerate(items, start=1):
            print(f"{index}. {item.strip()}")

def main():
    while True:
        first_choise = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no").strip()
        if first_choise.lower()=="exit":
                print("thank you for using the To-Do program, come back again soon")
                break
        elif first_choise.lower()=="y":
            item=input("Enter your To-Do item: ")
            add_item(item)
        elif first_choise.lower() =="n":
            second_choise = input("do you want to list your To-Do items? answer by 'y' for yes and 'n' for no").strip()
            if second_choise.lower()=="exit":
                print("thank you for using the To-Do program, come back again soon")
                break
            elif second_choise.lower()=="y":
                print("Your To-Do items:")
                view_items()
            elif second_choise.lower()=="n":
                continue
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")     

if __name__ == "__main__":
    main() 