# YouTube English Accent Classifier

This Streamlit application analyzes YouTube videos to classify English accents using a pre-trained deep learning model. It downloads videos, extracts audio, and predicts accents with confidence scores.

---

## Features
- Download YouTube videos directly  
- Extract audio from videos  
- Classify English accents (American, British, Australian, etc.)  
- Display results with confidence scores  
- Automatic cleanup of temporary files

---

## Project Structure
```

REMWaste_challenge/
├── app.py                # Main application script
├── utils/
│   ├── audio\_extractor.py    # Video download & audio extraction
│   └── classifier.py         # Model loading & accent classification
└── README.md

````

---

## Requirements
- Python 3.13
- FFmpeg (for audio processing)

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/ghiati/REMWaste_challenge.git
cd REMWaste_challenge
````

### 2. Install system dependencies

**FFmpeg Installation:**

* **Ubuntu/Debian:**

```bash
sudo apt update && sudo apt install ffmpeg
```

* **macOS (Homebrew):**

```bash
brew install ffmpeg
```

* **Windows:**
  Download FFmpeg from [https://ffmpeg.org](https://ffmpeg.org) and add it to your system PATH.

---

### 3. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

---

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at [http://localhost:8501](http://localhost:8501)

---

## Usage Guide

1. **Enter YouTube URL**: Paste a valid YouTube video URL ( to make the process fast use a short video)
2. **Click "Analyze Accent"**:

   * Application downloads the video
   * Extracts audio from the video
   * Analyzes the speaker's accent
3. **View Results**:

   * Detected accent type (e.g., British, American)
   * Confidence score percentage
4. **Try Another**: Enter a new URL to analyze another video