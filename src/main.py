import argparse

from dotenv import load_dotenv

import chat_gpt


def main(args: argparse.Namespace):
    load_dotenv()

    timeout = args.timeout
    gpt = chat_gpt.ChatGPT(timeout)

    gpt.request_to_gpt(prompt="こんにちは")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Config argument to set up ChatGPT")
    parser.add_argument("--model", action="store_true", help="Use GPT-4 or not")
    parser.add_argument(
        "-t", "--timeout", type=int, help="Timeout until receive response"
    )
    parser.add_argument(
        "-m", "--multi", action="store_true", help="Enable multi-line mode"
    )
    parser.add_argument("-r", "--raw", action="store_true", help="Enable raw mode")
    args = parser.parse_args()

    main(args)
