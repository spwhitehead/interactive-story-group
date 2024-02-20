import player
import items
import choices
import ai_functions
import json


def main():

    print()
    ai_functions.print_typing(
        "Hello, and welcome to the adventure game. Good luck. :)")
    print()
    player_name = input("What is your name? ")
    player.name_player(player_name)
    # clear the terminal screen here for immersion.
    # color the text for fun

    choices.play_scene(choices.initial_scene)


if __name__ == "__main__":
    main()
