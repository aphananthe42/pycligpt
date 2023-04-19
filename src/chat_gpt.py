import os

import openai


class ChatGPT:
    def __init__(self, timeout: float = 30):
        openai.api_key = os.environ["OPENAI_API_KEY"]
        self.timeout = timeout

    def request_to_gpt(self, prompt: str):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {"role": "user", "content": prompt},
            ],
        )
        print(response.choices[0]["message"]["content"].strip())
