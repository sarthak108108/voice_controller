import whisper
import speech_recognition as sr
import tempfile
import os
import re

model = whisper.load_model("tiny")

recogniser = sr.Recognizer()

def command_recon():
    with sr.Microphone() as source:
        recogniser.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")

        try:
            audio = recogniser.listen(source, timeout=1.5, phrase_time_limit=1.5)
            print("Audio captured, processing...")

            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
                temp_audio.write(audio.get_wav_data())
                temp_audio_path = temp_audio.name  

            print(temp_audio.name)

            result = model.transcribe(temp_audio_path)
            command = result["text"]
            command = command.lower()
            cleaned_command = re.sub(r'[^a-z\s]', '', command)
            first_word = cleaned_command.split()[0] if cleaned_command else ''
            print(f"Command recognized: {command}")
            os.remove(temp_audio_path)
            

            return first_word

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.WaitTimeoutError:
            print("Listening timed out")
        except Exception as e:
            print(f"An error occurred: {e}")

        return None
    
    