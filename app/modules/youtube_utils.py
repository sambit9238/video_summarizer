import os
import math
from pytube import YouTube
from moviepy.editor import AudioFileClip
from models import AudioInfo


def download_audio(youtube_url) -> AudioInfo:
    yt = YouTube(youtube_url)

    # Filter streams to only get audio with the highest quality
    audio_stream = yt.streams.filter(only_audio=True).order_by("abr").desc().first()

    # Download the audio
    print(f"Downloading audio from {yt.title}...")
    audio_file_path = audio_stream.download(filename=yt.title + "_audio")
    print("Download complete.")

    # Convert audio file to mp3 format
    audio = AudioFileClip(audio_file_path)
    mp3_file_path = os.path.splitext(audio_file_path)[0] + ".mp3"
    audio.write_audiofile(mp3_file_path, codec="mp3")

    # Calculate the length of the audio file in minutes and round it up
    audio_length_minutes = math.ceil(audio.duration / 60)
    print(
        f"The length of the audio file is approximately {audio_length_minutes} minutes."
    )

    audio.close()

    # Remove the original audio file
    os.remove(audio_file_path)
    print("Audio successfully converted to mp3 format.")

    audio_info = AudioInfo(
        audio_file_path=mp3_file_path, audio_length_minutes=audio_length_minutes
    )
    return audio_info
