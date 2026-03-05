# helpers/video_to_audio.py

from moviepy import VideoFileClip
import os

def video_to_audio(video_path: str, audio_output_path: str) -> str:
    """
    Convert video file to audio (MP3).
    """
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_output_path)
    audio.close()
    video.close()
    return audio_output_path
