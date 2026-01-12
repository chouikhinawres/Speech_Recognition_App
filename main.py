import streamlit as st
from audiorecorder import audiorecorder
import speech_recognition as sr
import tempfile

st.title("🎙️ Speech Recognition App (No PyAudio)")

audio = audiorecorder("Start Recording", "Stop Recording")

if len(audio) > 0:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        audio.export(f.name, format="wav")
        audio_path = f.name

    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)

        try:
            text = r.recognize_google(audio_data)
            st.success("Transcription:")
            st.write(text)
        except sr.UnknownValueError:
            st.error("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"API error: {e}")
