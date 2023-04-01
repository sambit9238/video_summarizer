import openai
from models import ChatCompletionInfo


class OpenAIUtils:

    WHISPER_COST_PER_MINUTE = 0.006
    GPT3_5_TURBO_COST_PER_1000_TOKENS = 0.002

    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def transcribe_audio(self, audio_file_path):
        """
        Whisper	$0.006 / minute (rounded to the nearest second)
        """
        # Load the audio file
        audio_file = open(audio_file_path, "rb")
        # Call the OpenAI API for transcription
        response = openai.Audio.transcribe("whisper-1", audio_file)
        # Extract the transcription
        transcription = response.get("text")
        return transcription

    def get_chat_completion(self, prompt, model="gpt-3.5-turbo") -> ChatCompletionInfo:
        response = openai.ChatCompletion.create(
            model=model,
            temperature=0,
            messages=[{"role": "user", "content": f"{prompt}"}],
        )
        summary = response.choices[0].message["content"]
        num_tokens = response.usage["total_tokens"]
        chat_completion_info = ChatCompletionInfo(
            chat_completion=summary, chat_completion_length=num_tokens
        )
        return chat_completion_info

    def calculate_cost(
        self, audio_duration_minutes: float, gpt3_5_turbo_tokens: int
    ) -> float:
        whisper_cost = audio_duration_minutes * self.WHISPER_COST_PER_MINUTE
        gpt3_5_turbo_cost = (
            gpt3_5_turbo_tokens / 1000
        ) * self.GPT3_5_TURBO_COST_PER_1000_TOKENS
        total_cost = whisper_cost + gpt3_5_turbo_cost
        return round(total_cost, 2)

    def get_summary(self, transcription) -> ChatCompletionInfo:
        prompt = f"I have a transcription from a video. Please provide a notes-like summary that highlights the key points, making it easy to learn and understand the main concepts. Givethe summary with appropriate html tags to make it easier to read in a website. The transcription is as follows: {transcription}"
        chat_completion_info = self.get_chat_completion(prompt)
        return chat_completion_info
