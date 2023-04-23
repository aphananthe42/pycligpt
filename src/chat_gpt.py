import getpass
import os

import openai

import color


class ChatGPT:
    def __init__(self, useGPT4: bool, timeout: float):
        openai.api_key = os.environ["OPENAI_API_KEY"]
        if useGPT4:
            self.model = "gpt-4"
        else:
            self.model = "gpt-3.5-turbo"
        self.timeout = timeout

    def print_greeting(self):
        print(color.Color.GREEN + f"Hello, {getpass.getuser()}🤖" + color.Color.END)
        print(
            color.Color.PURPLE
            + f"Current model: {self.model},\nTimeout: {self.timeout}"
            + color.Color.END
        )

    def send(self, prompt: str) -> dict[str, str]:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {"role": "user", "content": prompt},
            ],
            timeout=self.timeout,
        )

        reply = response.choices[0].message.content.strip()
        consumed_token = response.usage.total_tokens
        answer = {"reply": reply, "consumed_tokens": consumed_token}

        return answer
