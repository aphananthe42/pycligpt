import os
from datetime import datetime

import openai


class ChatGPT:
    def __init__(self, timeout: float):
        openai.api_key = os.environ["OPENAI_API_KEY"]
        self.timeout = timeout

    def request_to_gpt(self, prompt: str):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant.\nKnowledge cutoff: 2021-09\nCurrent date: {datetime.now().strftime('%Y-%m-%d')}",
                },
                {"role": "user", "content": prompt},
            ],
        )
        print(response.choices[0]["message"]["content"].strip())
