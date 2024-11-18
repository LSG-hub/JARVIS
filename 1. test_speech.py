import speech_recognition as sr

def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default system microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            # Capture the audio
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing...")
            # Recognize the speech using Google's Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            # Speech was unintelligible
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            # Could not request results from Google Speech Recognition service
            print(f"Could not request results; {e}")
        except sr.WaitTimeoutError:
            # Listening timed out while waiting for phrase
            print("Listening timed out. Please try again.")

if __name__ == "__main__":
    recognize_speech()
