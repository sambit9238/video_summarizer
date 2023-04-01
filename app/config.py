import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "your_openai_api_key_here")

AUDIO_FORMAT = "mp3"
TRANSCRIPTION_MODEL = "whisper"
SUMMARY_MODEL = "gpt-3.5-turbo"
