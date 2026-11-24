
import pyttsx3


def speak_text(text):

    if not text:
        return

    try:
        # Initialize voice engine
        engine = pyttsx3.init("sapi5")

        # Set speaking speed
        engine.setProperty("rate", 170)

        # Set voice volume
        engine.setProperty("volume", 1.0)

        print("Assistant is speaking...")

        # Convert text into speech
        engine.say(text)

        # Play the speech
        engine.runAndWait()

        # Stop the engine
        engine.stop()

        print("Speech finished!")

    except Exception as e:
        print("Text-to-Speech Error:", e)


# Test text-to-speech
if __name__ == "__main__":

    print("Text-to-Speech Started!")

    speak_text("Hello Khushi! Your AI voice assistant is working.")

    print("Test completed!")
