# helpers/audio_to_text.py

import speech_recognition as sr
from pydub import AudioSegment

def audio_to_text(audio_path: str) -> str:
    """
    Transcribe audio file to text.
    """
    # Convert to WAV if needed
    if audio_path.endswith(".mp3"):
        audio = AudioSegment.from_mp3(audio_path)
        wav_path = audio_path.replace(".mp3", ".wav")
        audio.export(wav_path, format="wav")
        audio_path = wav_path

    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
        try:
            text = r.recognize_google(audio)
        except sr.RequestError:
            text = "API error: Could not request results."
        except sr.UnknownValueError:
            text = "Could not understand audio."

    return text
