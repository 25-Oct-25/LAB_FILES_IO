import os
import sys

FILENAME = "to_do.txt"

def add_item(text):
    # append the item as a new line
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(text.strip() + "\n")

def list_items():
    if not os.path.exists(FILENAME):
        print("No to-do items yet.")
        return
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    if not lines:
        print("No to-do items yet.")
    else:
        for i, line in enumerate(lines, start=1):
            print(f"{i}- {line}")

def main():
    print("Welcome to To-Do. Type 'exit' any time to quit.")
    while True:
        ans = input("Do you want to add a new To-Do item? (y/n): ").strip().lower()
        if ans == "exit":
            break
        if ans == "y":
            item = input("Type your new To-Do item: ").strip()
            if item.lower() == "exit":
                break
            if item:
                add_item(item)
                print("Saved.")
            else:
                print("Empty item, not saved.")
            # after adding, go back to first question (loop continues)
            continue
        if ans == "n":
            ans2 = input("Do you want to list your To-Do items? (y/n): ").strip().lower()
            if ans2 == "exit":
                break
            if ans2 == "y":
                list_items()
            # else do nothing and loop again to first question
            continue
        # if user typed something else
        print("Please answer 'y' or 'n' (or type 'exit').")

    # on exit
    print("thank you for using the To-Do program, come back again soon")

if __name__ == "__main__":
    main()