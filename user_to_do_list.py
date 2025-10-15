
while True:
    user_input = input("Do you want add a new item? type 'y' for yes, and 'n' for no")
    if user_input == 'y':
        user_input_list = input("You can type your item now: ")
        file = open('to_do.txt', 'a+', encoding="UTF-8")
        file.write(user_input_list + '\n')
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


