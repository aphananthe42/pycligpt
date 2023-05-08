import getpass
import os

import openai

import color


class ChatGPT:
    def __init__(self, useGPT4: bool, timeout: float):
        openai.api_key = os.environ["OPENAI_API_KEY"]
        self.model = "gpt-4" if useGPT4 else "gpt-3.5-turbo"
        self.messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            }
        ]
        self.timeout = timeout

    def print_greeting(self):
        print(color.Color.GREEN + f"Hello, {getpass.getuser()}🤖" + color.Color.END)
        print(
            color.Color.PURPLE
            + f"Current model: {self.model},\nTimeout: {self.timeout}"
            + color.Color.END
        )

    def send(self, prompt: str) -> dict[str, str]:
        self.messages.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            timeout=self.timeout,
        )

        reply = response.choices[0].message.content.strip()
        consumed_token = response.usage.total_tokens
        answer = {"reply": reply, "consumed_tokens": consumed_token}

        self.messages.append({"role": "assistant", "content": reply})

        return answer
