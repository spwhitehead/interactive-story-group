import openai

# Your OpenAI API key
openai.api_key_path = "/Users/spencerwhitehead/Desktop/Code/Assignments/interactive-story-group/API-Key.txt"


def chat_with_gpt(prompt):
    try:
        # Making a request to the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model you want to use
            messages=[
                {"role": "system", "content": "accept a simple story about something from a user, then give a hypothetical story in return as if the opposite in the story had happened. For example, if someone says 'I sold my favorite car in college' you could return a hypothetical short story about what would have happened if they had kept the car. The story should be 3-5 sentences long."},
                {"role": "user", "content": prompt},
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return str(e)


# Example usage
user_input = input("Say something to ChatGPT: ")
response = chat_with_gpt(user_input)
print("ChatGPT:", response)
