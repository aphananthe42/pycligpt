from dotenv import load_dotenv

import chat_gpt


def main():
    load_dotenv()
    gpt = chat_gpt.ChatGPT(timeout=60)
    gpt.request_to_gpt(prompt="こんにちは")


if __name__ == "__main__":
    main()
