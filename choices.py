import json
import ai_functions
import main
# Load the adventure JSON data


def load_adventure_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)


# Display the current scene and process user input
adventure_data = load_adventure_data('adventure.json')


def play_scene(scene):
    previous_scene = adventure_data['scenes'][scene['id'] - 1]
    print(ai_functions.have_AI_describe(
        scene['description'], previous_scene['description']))
    if 'ending' in scene and scene['ending']:
        print()
        print("Thank you for playing.")
        return
    for idx, choice in enumerate(scene['choices'], start=1):
        print(f"{idx}. {choice['text']}")
    user_choice = input("What do you choose? ")
    user_choice = int(ai_functions.have_AI_choose(
        scene['choices'], user_choice)) - 1
    if 'add_item' in scene['choices'][user_choice]:
        main.player1.add_item(scene['choices'][user_choice]['add_item'])
        print(f"You picked up {scene['choices'][user_choice]['add_item']}")
    if user_choice == "x":
        ai_functions.have_conversation_with(scene['characters'][0])
        for idx, choice in enumerate(scene['choices'], start=1):
            print(f"{idx}. {choice['text']}")
        user_choice = input("What do you choose? ")
        user_choice = int(ai_functions.have_AI_choose(
            scene['choices'], user_choice)) - 1
    next_scene_id = scene['choices'][user_choice]['leads_to']
    next_scene = next(
        filter(lambda x: x['id'] == next_scene_id, adventure_data['scenes']), None)
    if next_scene:
        play_scene(next_scene)
    else:
        print("Error: Scene not found.")


# Load the adventure data

# Start the adventure
# Assuming the first scene is the starting point
initial_scene = adventure_data['scenes'][0]
