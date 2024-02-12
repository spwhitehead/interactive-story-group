import openai

# Your OpenAI API key
with open("API-Key.txt", "r") as file:
    api_key = file.read().strip()


def chat_with_gpt(prompt):
    try:
        # Making a request to the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model you want to use
            messages=[
                {"role": "system", "content": "You are a story teller who tells what would happen if whatever the user tells you didn't actually happen."},
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
