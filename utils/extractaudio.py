import os
import yt_dlp
from moviepy import VideoFileClip

def download_video(url, out_file="downloaded_video.mp4"):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': out_file,
        'quiet': True,
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return out_file

def extract_audio(video_file, audio_file="audio.wav"):
    clip = VideoFileClip(video_file)
    if clip.audio is None:
        clip.close()
        raise RuntimeError(f"No audio stream found in {video_file}")
    
    clip.audio.write_audiofile(audio_file)
    clip.close()
    return audio_file