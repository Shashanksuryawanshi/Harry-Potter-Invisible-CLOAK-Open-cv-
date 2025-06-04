# Inside voice_activation.py

import speech_recognition as sr
import streamlit as st

def listen_for_keyword(keyword="make me invisible"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.info("🎙 Listening for voice command: 'Make me invisible!'")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

    try:
        transcript = recognizer.recognize_google(audio).lower()
        st.success(f"✅ You said: {transcript}")
        return keyword in transcript
    except sr.UnknownValueError:
        st.warning("🤔 Couldn't understand the command.")
    except sr.RequestError:
        st.error("❌ Could not request results. Check internet.")
    return False
