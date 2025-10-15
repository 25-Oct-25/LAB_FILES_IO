# Lab 11 - To-Do List
import time

file_path = "Lab11/Lab/To_do.txt"

def add_task(task):
    
    """Add a new tasks"""
    
    with open(file_path, "a", encoding="utf-8") as file:
        date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file.write(f"{task} (added on {date_time})\n")
    print("✅ Task added successfully!\n")

def show_tasks():
    """Show All Tasks"""
    
    try:
        
        with open(file_path, "r", encoding="utf-8") as file:
           
            tasks = file.readlines()
           
            if not tasks:
                print("No tasks found.\n")
            else:
                print("\n========= To-Do List =========")
                for task in tasks:
                    print("📌", task.strip())
                print("==============================\n")
  
    except FileNotFoundError:
        print("No to-do file found yet.\n")

def main():
    
    print("Welcome to the To-Do Program! 📝")
    
    while True:
        
        user_input = input(
            'Do you want to add a new To-Do item? (y/n) or type "exit" to quit: '
        ).lower()

        if user_input == "exit":
            print("🙏 Thank you for using the To-Do program, come back again soon!")
            break

        elif user_input == "y":
            task = input("Enter your new task: ")
            add_task(task)

        elif user_input == "n":
            read_choice = input("Do you want to list your To-Do items? (y/n): ").lower()
            if read_choice == "y":
                show_tasks()
            else:
                print("Okay, maybe later.\n")

        else:
            print("Invalid choice, please type y, n, or exit.\n")

# Run the program
main()
