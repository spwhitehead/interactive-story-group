import player
import items
import mechanics
import choices
import ai_functions
import json



def main():
    
    print("Hello, and welcome to the adventure game. Good luck. :)")
    player_name = input("What is your name? ")
    player1 = player.Player(player_name)
    
    # clear the terminal screen here for immersion.
    # color the text for fun
    
    

    choices.play_scene(choices.initial_scene)














    # print("You wake up and slowly open your eyes. You see...")
    # ai_functions.have_AI_describe("Describe the first room of the adventure game. It has two doors and a key.")

    # print("Gameplay Mechanics: Enter a number to select an option.")
    # print("1. Open the door")
    # print("2. Open the door")
    # print("3. Look around")
    # choice = input("What is your choice? ")

    # if choice == "1":
    #     pass
    # elif choice == "2":
    #     pass
    # elif choice == "3":
    #     ai_functions.have_AI_describe("Describe the room. Which will be mostly empty but is cold and damp, and there is a bucket inside the room.")
    #     mechanics.print_choices(choices.room1_look_around_choices)
    #     choice = input("What is your choice? ")
    #     if choice == "1":
    #         print("You look in the bucket. You see...")
    #         ai_functions.have_AI_describe("Describe the item in the bucket. It is a small key. It is covered in something.")
    #         mechanics.print_choices(choices.room1_bucket_choices)
    #         choice = input("What is your choice? ")
    #         if choice == "1":
    #             print("You grab the key. You put it in your pocket.")
    #             player1.add_item(items.Key("key", "a small key"))
    #             ai_functions.have_AI_describe("Describe the way the key felt going into your pocket.")
    #             mechanics.print_choices(choices.room1_key_choices)
    #         elif choice == "2":
    #             pass
    #         elif choice == "3":
    #             pass
    #         elif choice == "4":
    #             pass
    #         else:
    #             print("Invalid input. Please select a valid option.")
    #             main()
    #     elif choice == "2":
    #         pass
    #     elif choice == "3":
    #         pass
    #     elif choice == "4":
    #         pass
    #     else:
    #         print("Invalid input. Please select a valid option.")
    #         main()


if __name__ == "__main__":
    main()
