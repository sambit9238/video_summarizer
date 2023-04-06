# FastAPI Video Summary Service

This is a FastAPI web application that provides an API to summarize video content. The service utilizes the OpenAI API to generate text summaries of the video transcriptions.

## Table of Contents

1. [Installation](#installation)
2. [Endpoints](#endpoints)
    - [POST /api/video_summary](#post-apivideo_summary)
    - [GET /](#get-)
3. [Schema](#schema)
    - [VideoSummaryRequest](#videosummaryrequest)
    - [VideoSummaryResponse](#videosummaryresponse)

## Installation

1. Clone the repository: git clone https://github.com/yourusername/fastapi-video-summary.git
2. Navigate to the project directory: cd fastapi-video-summary
3. Create a virtual environment and activate it:  

```
python3 -m venv devenv 
source devenv/bin/activate
```
4. Install the required packages:
```
pip install -r requirements.txt
```
5. Run the application
```
python3 app/main.py
```

## Endpoints
### POST /api/video_summary

Generates a text summary of the video content.

Request body:

- `openai_api_key` (string, required): Your OpenAI API key.
- `video_url` (string, required): The URL of the video to summarize.

Response:

- `video_url` (string): The URL of the video.
- `transcription` (string): The transcription of the video's content.
- `summary` (string): The generated summary of the video's content.
- `approximate_cost` (string): The approximate cost of the API call in USD.

### GET /

Returns a successful response when the application is running.

## Schema

### VideoSummaryRequest

- `openai_api_key` (string, required): Your OpenAI API key.
- `video_url` (string, required): The URL of the video to summarize.

### VideoSummaryResponse

- `video_url` (string): The URL of the video.
- `transcription` (string): The transcription of the video's content.
- `summary` (string): The generated summary of the video's content.
- `approximate_cost` (string): The approximate cost of the API call in USD.
