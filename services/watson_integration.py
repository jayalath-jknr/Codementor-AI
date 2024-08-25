import os
import requests
import subprocess
from dotenv import load_dotenv

load_dotenv()

class WatsonIntegration:
    def __init__(self):
        self.api_key = os.getenv('WATSON_API_KEY')
        self.url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
        self.model_id = "ibm/granite-20b-code-instruct"
        self.project_id = "8719a597-19da-440a-8a0b-e7738acef74d"

    def generate_code(self, prompt):
        body = {
            "input": prompt,
            "parameters": {
                "decoding_method": "greedy",
                "max_new_tokens": 200,
                "repetition_penalty": 1
            },
            "model_id": self.model_id,
            "project_id": self.project_id
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.post(self.url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["text"]

    def review_code(self, code_snippet):
        prompt = f"Review the following C++ code:\n\n{code_snippet}"
        return self.generate_code(prompt)

    def execute_code(self, code_snippet):
        try:
            with open("temp_code.cpp", "w") as code_file:
                code_file.write(code_snippet)
            compile_result = subprocess.run(["g++", "temp_code.cpp", "-o", "temp_code"], capture_output=True, text=True)
            if compile_result.returncode != 0:
                return compile_result.stderr, False
            run_result = subprocess.run(["./temp_code"], capture_output=True, text=True)
            return run_result.stdout, True
        except Exception as e:
            return str(e), False

    def correct_code(self, error_message):
        prompt = f"Correct the following C++ code error: {error_message}"
        return self.generate_code(prompt)
