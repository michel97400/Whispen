import requests
from dotenv import load_dotenv
import os

class WhisperTranscriber:
    def __init__(self, endpoint=None, api_key=None, model_name=None, language="fr"):
        load_dotenv("BACKEND/.env")
        self.endpoint = endpoint or "https://ai-speech-michel.cognitiveservices.azure.com/openai/deployments/whisper/audio/transcriptions?api-version=2024-06-01"
        self.api_key = api_key or os.environ.get('WHISPER_API_KEY')
        self.model_name = model_name or "whisper (version:001)"
        self.language = language
        if not self.api_key:
            raise ValueError("WHISPER_API_KEY non trouvée dans l'environnement")

    def transcribe(self, audio_path):
        headers = {
            "api-key": self.api_key,
        }
        with open(audio_path, "rb") as audio_file:
            files = {
                "file": audio_file,
                "model": (None, self.model_name),
                "response_format": (None, "text"),
                "language": (None, self.language)
            }
            response = requests.post(self.endpoint, headers=headers, files=files)
        response.raise_for_status()
        return response.text

