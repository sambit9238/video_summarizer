from pydantic import BaseModel


class VideoSummaryRequest(BaseModel):
    openai_api_key: str
    video_url: str
