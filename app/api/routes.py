from fastapi import APIRouter, HTTPException
from modules import OpenAIUtils, download_audio
from models import VideoSummaryRequest, VideoSummaryResponse

router = APIRouter()


@router.post("/video_summary", response_model=VideoSummaryResponse, status_code=200)
async def video_summary(request: VideoSummaryRequest):
    try:
        # Download YouTube audio
        audio_info = download_audio(request.video_url)

        openai_app = OpenAIUtils(request.openai_api_key)
        # Transcribe the audio file
        transcribed_text = openai_app.transcribe_audio(
            audio_file_path=audio_info.audio_file_path
        )

        # Generate a summary from the transcription
        summary_info = openai_app.get_summary(transcription=transcribed_text)

        approximate_cost = openai_app.calculate_cost(
            audio_duration_minutes=audio_info.audio_length_minutes,
            gpt3_5_turbo_tokens=summary_info.chat_completion_length,
        )

        # Create and return the response object
        response = VideoSummaryResponse(
            video_url=request.video_url,
            transcription=transcribed_text,
            summary=summary_info.chat_completion,
            approximate_cost=f"{approximate_cost}USD",
        )
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


"""
We define a video_summary route that accepts a POST request with a JSON payload containing the YouTube URL and OpenAI API key. This route performs the following steps:

1. Download the audio from the YouTube video.
2. Convert the audio to the desired format.
3. Transcribe the audio using the OpenAI API.
4. Generate a summary of the transcription using the OpenAI API.

Finally, we return a JSON response containing the YouTube URL, transcription, and summary. If an error occurs during any of the steps, an HTTP 500 Internal Server Error is raised with a relevant error message.
"""
