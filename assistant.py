
# Import required functions
from speech_to_text import listen_to_voice
from groq_client import get_ai_response
from text_to_speech import speak_text


# Main voice assistant function
def start_assistant():

    print("\n================================")
    print("     AI VOICE ASSISTANT")
    print("================================")

    speak_text("Hello Khushi! Your voice assistant is ready.")

    while True:

        # Step 1: Listen to user voice
        user_input = listen_to_voice()

        # Check if voice is recognized
        if not user_input:
            continue

        # Step 2: Exit condition
        if user_input.strip().lower() in ["exit", "stop", "goodbye"]:
            speak_text("Goodbye Khushi! Have a nice day.")
            print("Assistant stopped.")
            break

        # Step 3: Get AI response from Groq
        print("\nThinking...")

        assistant_reply = get_ai_response(user_input)

        # Step 4: Display AI response
        print("\nAssistant:", assistant_reply)

        # Step 5: Speak AI response
        speak_text(assistant_reply)


if __name__ == "__main__":
    start_assistant()
