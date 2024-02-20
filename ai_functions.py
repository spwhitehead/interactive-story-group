# Functions for the AI Api so that we can just run function in our game instead of having to type out a bunch of API stuff everytime.

from openai import OpenAI
import time

with open("openai-api-key.txt", "r") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)


def print_typing(response):
    for char in response:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()


def have_AI_describe(basic_scene_description, previous_scene):
    # Combine the basic scene description with the extra context
    # Make a call to OpenAI's API with the combined prompt
    if basic_scene_description == previous_scene:
        response = client.chat.completions.create(
            # You might need to change the engine based on availability and your needs
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a narrator for an interactive story game and are speaking to the player about the current scene of the game. You are to take in the basic descriptions of scenes of the game and describe them in more detail. Never add characters or items that arent explicitely talked about in the basic description. Keep it engaging and concise. Only 3 sentences max."},
                {"role": "user", "content": basic_scene_description}
            ]
        )
    else:
        response = client.chat.completions.create(
            # You might need to change the engine based on availability and your needs
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a narrator for an interactive story game and are speaking to the player about the current scene of the game. You are to take in the basic descriptions of scenes of the game and describe them in more detail. Never add characters or items that arent explicitely talked about in the basic description. Keep it engaging and concise. Only 3 sentences max. Also start with a sentence about the action the player is taking as they are move between scenes. The previous scene description was: {previous_scene}"},
                {"role": "user", "content": basic_scene_description}
            ]
        )

    # Extracting the text from the response object
    ai_response = response.choices[0].message.content.strip()
    return ai_response


def have_AI_choose(scene_choices, user_choice):
    choices = ""
    for i, choice in enumerate(scene_choices):
        choices += f"{i + 1}. {choice['text']}, "

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are an assistant for a narrator to an interactive story game. Your job is to take in an answer from the player about what they want to do, compare it to the available options and return a number if the players response is similar to the respective option. The available options for this scene are, {
                choices}. Each option is numbered. ONLY return the number of the option that the players response is similar to. Do not include any additional text. Just a single number nothing else. Your response will be used in code and needs to be only a single number."},
            {"role": "user", "content": f"{user_choice}"}
        ]
    )

    ai_response = response.choices[0].message.content.strip()
    return ai_response
