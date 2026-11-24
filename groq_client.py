
# Import required libraries
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key
api_key = os.getenv("Groq_api_key")

if not api_key:
    raise ValueError("Groq API key not found in .env file")

# Connect to Groq
client = Groq(api_key=api_key)

# Select AI model
MODEL = "openai/gpt-oss-20b"

# Create conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Answer in simple language."
    }
]


# Function to get AI response
def get_ai_response(user_input):

    # Add user message to history
    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        # Send conversation to Groq
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0
        )

        # Get assistant response
        assistant_reply = response.choices[0].message.content

        # Add response to conversation history
        messages.append({
            "role": "assistant",
            "content": assistant_reply
        })

        # Return AI response
        return assistant_reply

    except Exception as e:
        print("Groq API Error:", e)
        return "Sorry, I am unable to generate a response."


# Test the Groq connection
if __name__ == "__main__":

    print("Groq AI Assistant Started!")
    print("Type 'exit' to stop.\n")

    while True:

        user_input = input("You: ")

        if user_input.strip().lower() == "exit":
            print("Chat ended!")
            break

        answer = get_ai_response(user_input)

        print("Assistant:", answer)
