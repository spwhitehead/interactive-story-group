def print_choices(choices):
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

def choose():
    while True:
        choice = input("Choose an option: ")
        if choice == "1":
            print("You chose option 1")
            break
        elif choice == "2":
            print("You chose option 2")
            break
        else:
            print("Invalid choice. Please try again.")

