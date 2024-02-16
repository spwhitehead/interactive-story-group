import json

# Load the adventure JSON data


def load_adventure_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Display the current scene and process user input


def play_scene(scene):
    print(scene['description'])
    if 'ending' in scene and scene['ending']:
        print("The adventure ends here.")
        return
    for idx, choice in enumerate(scene['choices'], start=1):
        print(f"{idx}. {choice['text']}")
    user_choice = int(input("What do you choose? ")) - 1
    next_scene_id = scene['choices'][user_choice]['leads_to']
    next_scene = next(
        filter(lambda x: x['id'] == next_scene_id, adventure_data['scenes']), None)
    if next_scene:
        play_scene(next_scene)
    else:
        print("Error: Scene not found.")


# Load the adventure data
adventure_data = load_adventure_data('adventure.json')

# Start the adventure
# Assuming the first scene is the starting point
initial_scene = adventure_data['scenes'][0]
play_scene(initial_scene)
