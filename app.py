import os
import torch
import streamlit as st

# CRITICAL: These must be set BEFORE any other imports
os.environ['STREAMLIT_SERVER_FILE_WATCHER_TYPE'] = 'none'
os.environ['STREAMLIT_SERVER_ENABLE_WATCHER_DEFAULT'] = 'false'
os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'

# Monkey patch torch
def patch_torch_classes():
    try:
        import torch
        if hasattr(torch, 'classes') and hasattr(torch.classes, '__path__'):
            torch.classes.__path__ = None
    except:
        pass

patch_torch_classes()

# Set PyTorch to single-threaded mode
torch.set_num_threads(1)

# Configure Streamlit
st.set_page_config(
    page_title="YouTube English Accent Classifier",
    page_icon="🇬🇧"
)

# Import utils
from utils.extractaudio import download_video, extract_audio
from utils.classified_accent import load_accent_classifier, classify_accent

# Main Streamlit App
def main():
    st.title("🇬🇧 YouTube English Accent Classifier")
    st.write("Enter a YouTube URL to analyze the speaker's English accent")

    st.info("⏳ Please wait, the model is loading now...")
    with st.spinner("Loading accent classification model..."):
        accent_classifier = load_accent_classifier()
    
    if accent_classifier is not None:
        st.success("✅ Model loaded successfully!")
    else:
        st.error("Failed to load the accent classification model. Please try again.")
        return
    
    youtube_url = st.text_input("YouTube URL:", placeholder="https://www.youtube.com/watch?v=...")
    
    if st.button("Analyze Accent"):
        if not youtube_url:
            st.error("Please enter a YouTube URL")
            return
        
        try:
            with st.spinner("Processing video..."):
                st.info("📥 Downloading video...")
                video_file = download_video(youtube_url, "temp_video.mp4")
                
                st.info("🎵 Extracting audio...")
                audio_file = extract_audio(video_file, "temp_audio.wav")
                
                st.info("🔍 Analyzing accent...")
                label, score = classify_accent(accent_classifier, audio_file)
                
            if label and score:
                st.success("Analysis Complete!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Detected Accent", label)
                with col2:
                    st.metric("Confidence Score", f"{score:.1f}%")
                
                try:
                    os.remove(video_file)
                    os.remove(audio_file)
                except:
                    pass
                    
            else:
                st.error("Failed to classify the accent. Please try another video.")
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            for temp_file in ["temp_video.mp4", "temp_audio.wav"]:
                try:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
                except:
                    pass

if __name__ == "__main__":
    main()