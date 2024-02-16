from openai import OpenAI

client = OpenAI(api_key=input("Enter your OpenAI API key: "))

# Function to interact with ChatGPT and play the DND game


def play_dnd_game():
    initial_game_prompt = "Sample Message"  # Add initial game prompt here
    print("")  # Add welcome message to the user
    print()
    print(initial_game_prompt)
    print()
    game_history = [
        # Initial instructions for the AI
        {"role": "system", "content": "asdfasdf"},
        {"role": "user", "content": initial_game_prompt}
    ]
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye! Thanks for playing.")
            break
        else:
            game_history.append({"role": "user", "content": user_input})
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo", messages=game_history)

                game_response = response.choices[0].message.content.strip()
                print("Game Master:", game_response)
                game_history.append(
                    {"role": "assistant", "content": game_response})
            except Exception as e:
                print(str(e))

# Main function


def main():
    play_dnd_game()


if __name__ == "__main__":
    main()
