import os
from dotenv import load_dotenv, find_dotenv
from google import genai
from google.genai import types

# Load the Env files
load_dotenv(find_dotenv())

# Load the client
client = genai.Client()

# Keep History
history = []

MODEL = 'gemini-3.8-flash'
MAX_RETRIES = 4
DELAY = 1.5


# Prepare the bot
def chat(user_input):
    user_message = types.Content(role="user", parts=[types.Part(text=user_input)])
    contents = history + [user_message]

    history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))
    response = client.models.generate_content(
        model=MODEL,
        contents=history,
        config=types.GenerateContentConfig(temperature=0),
    )
    history.append(types.Content(role="model", parts=[types.Part(text=response.text)]))
    return response.text

# User responses

if __name__ == '__main__':
    while True:
        user_input = input("Write a message... ")
        if user_input.lower() in {"quit", "exit", "close"}:
            break
        print("Response:", chat(user_input))