import librosa
import streamlit as st
from transformers import pipeline

@st.cache_resource(show_spinner=False)
def load_accent_classifier():
    try:
        return pipeline(
            "audio-classification",
            model="dima806/english_accents_classification",
            feature_extractor_kwargs={"sampling_rate": 16000}
        )
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def classify_accent(accent_classifier, audio_path):
    try:
        preds = accent_classifier(audio_path)
        label = preds[0]["label"]
        score = preds[0]["score"] * 100
        return label, score
    except Exception as e:
        if "ffmpeg" in str(e).lower():
            try:
                audio_array, sample_rate = librosa.load(audio_path, sr=16000)
                preds = accent_classifier(audio_array)
                label = preds[0]["label"]
                score = preds[0]["score"] * 100
                return label, score
            except Exception as librosa_error:
                st.error(f"Error with librosa fallback: {str(librosa_error)}")
                return None, None
        else:
            st.error(f"Error classifying audio: {str(e)}")
            return None, None