# Functions for the AI Api so that we can just run function in our game instead of having to type out a bunch of API stuff everytime.

import openai

client = openai.Client(api_key="YOUR_API_KEY_HERE")

def have_AI_describe(prompt):
    response = client.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response

def have_conversation_with(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=prompt
    )
    return response

 
