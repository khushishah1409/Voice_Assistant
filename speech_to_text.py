
import speech_recognition as sr


def listen_to_voice():

    # Create recognizer object
    recognizer = sr.Recognizer()

    # Access microphone
    with sr.Microphone() as source:

        print("Listening... Speak something!")

        # Adjust for background noise
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            # Capture voice
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

            print("Processing your voice...")

            # Convert speech into text
            text = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print("You said:", text)

            return text

        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Sorry, I could not understand your voice.")

        except sr.RequestError as e:
            print("Speech recognition error:", e)

        except Exception as e:
            print("Error:", e)

    return None


# Test speech recognition
if __name__ == "__main__":
    listen_to_voice()
