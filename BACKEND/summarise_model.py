from openai import OpenAI
from dotenv import load_dotenv
import os

class Assistant_summarise:
    def __init__(self, endpoint=None, deployment_name=None, api_key=None):
        load_dotenv()
        self.endpoint = "https://ia-michel.services.ai.azure.com/openai/v1/"
        self.deployment_name = deployment_name or "grok-4-fast-non-reasoning"
        self.api_key = api_key or os.environ.get('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY non trouvée dans l'environnement")
        self.client = OpenAI(
            base_url=self.endpoint,
            api_key=self.api_key
        )

    def ask(self, user_input):
        messages = [
            {
                "role": "system",
                "content": "Résumes le texte . Sois précis et résume en quelques phrases. Commence par 'Le texte parle de"
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
        completion = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=messages
        )
        return completion.choices[0].message.content

