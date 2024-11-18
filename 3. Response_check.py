import speech_recognition as sr
import pyttsx3

def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Use the default system microphone as the audio source
    with sr.Microphone() as source:
        print("Listening for the wake word 'Jarvis'...")
        engine.say("Listening for the wake word 'Jarvis'")
        engine.runAndWait()
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        while True:
            try:
                # Capture the audio
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                # Recognize the speech using Google's Web Speech API
                text = recognizer.recognize_google(audio).lower()
                
                # Check for the wake word "Jarvis"
                if "jarvis" in text:
                    print("Wake word 'Jarvis' detected. How can I assist you?")
                    engine.say("Wake word Jarvis detected. How can I assist you?")
                    engine.runAndWait()
                    break
                else:
                    print("Waiting for the wake word 'Jarvis'...")
            except sr.UnknownValueError:
                # Speech was unintelligible
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                # Could not request results from Google Speech Recognition service
                print(f"Could not request results; {e}")
            except sr.WaitTimeoutError:
                # Listening timed out while waiting for phrase
                print("Listening timed out. Please try again.")

    # Once the wake word is detected, listen for the next command
    with sr.Microphone() as source:
        print("Listening for your command...")
        engine.say("Listening for your command")
        engine.runAndWait()
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            engine.say(f"You said: {text}")
            engine.runAndWait()
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            engine.say("Sorry, I could not understand the audio.")
            engine.runAndWait()
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            engine.say(f"Could not request results; {e}")
            engine.runAndWait()
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
            engine.say("Listening timed out. Please try again.")
            engine.runAndWait()

if __name__ == "__main__":
    recognize_speech()
