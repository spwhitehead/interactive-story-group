import json
import ai_functions
import player
# Load the adventure JSON data


def load_adventure_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)


# Display the current scene and process user input
adventure_data = load_adventure_data('adventure.json')


def play_scene(scene):
    previous_scene = adventure_data['scenes'][scene['id'] - 1]
    print()
    ai_functions.print_typing(ai_functions.have_AI_describe(
        scene['description'], previous_scene['description']))
    if 'ending' in scene and scene['ending']:
        print()
        ai_functions.print_typing("Thank you for playing.")
        return
    for idx, choice in enumerate(scene['choices'], start=1):
        print(f"{idx}. {choice['text']}")
    print()
    user_choice = input("What do you choose? ")
    if user_choice == "Print Items":
        player.player1.print_items()
    user_choice = int(ai_functions.have_AI_choose(
        scene['choices'], user_choice)) - 1
    if 'add_item' in scene['choices'][user_choice]:
        player.player1.add_item(scene['choices'][user_choice]['add_item'])
        print()
        ai_functions.print_typing(
            f"You picked up {scene['choices'][user_choice]['add_item']}")
    if 'required_items' in scene['choices'][user_choice]:
        if not player.player1.check_items(scene['choices'][user_choice]['required_items']):
            print()
            ai_functions.print_typing("You don't have the required items.")
            play_scene(scene)
    next_scene_id = scene['choices'][user_choice]['leads_to']
    next_scene = next(
        filter(lambda x: x['id'] == next_scene_id, adventure_data['scenes']), None)
    if next_scene:
        play_scene(next_scene)
    else:
        ai_functions.print_typing("Error: Scene not found.")


# Load the adventure data

# Start the adventure
# Assuming the first scene is the starting point
initial_scene = adventure_data['scenes'][0]
