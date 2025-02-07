import speech_recognition as sr
from openai import OpenAI

recogniser = sr.Recognizer()
convertor = OpenAI()

def command_recon():
    with sr.Microphone() as source:
        recogniser.adjust_for_ambient_noise(source, duration = 0.5)
        print("listening...")

        try:
            audio = recogniser.listen(source, timeout = 0.5, phrase_time_limit=0.5)
            print("Auio is captured : processing...")

            command = convertor.audio.transcription.create(
                model = 'whisper-1',
                file = audio
            )
            print('command recognised, command : $s', command)
            return command
        except sr.UnknownValueError:
            return None
        except sr.WaitTimeoutError:
            return None

