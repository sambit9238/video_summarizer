from pydantic import BaseModel


class AudioInfo(BaseModel):
    audio_file_path: str
    audio_length_minutes: int


class ChatCompletionInfo(BaseModel):
    chat_completion: str
    chat_completion_length: int
