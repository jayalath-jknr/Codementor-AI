import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FalconIntegration:
    def __init__(self):
        self.api_key = os.getenv('AI71_API_KEY')
        self.base_url = "https://api.ai71.ai/v1/completions"

    def get_feedback(self, message):
        response = requests.post(
            self.base_url,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": "falcon",
                "prompt": message,
                "max_tokens": 200
            }
        )
        response.raise_for_status()
        return response.json()["choices"][0]["text"]
