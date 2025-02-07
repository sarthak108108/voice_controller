import speech_recognition as sr

recogniser = sr.Recognizer()

def command_recon():
    with sr.Microphone() as source:
        recogniser.adjust_for_ambient_noise(source, duration = 0.7)
        print("listening...")

        try:
            audio = recogniser.listen(source, timeout = 0.5, phrase_time_limit=0.5)
            command = recogniser.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            return None
        except sr.WaitTimeoutError:
            return None

