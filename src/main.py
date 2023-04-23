import argparse

from dotenv import load_dotenv

import chat_gpt
import color


def main(args: argparse.Namespace):
    load_dotenv()

    gpt = chat_gpt.ChatGPT(args.gpt4, args.timeout)
    gpt.print_greeting()

    while True:
        try:
            prompt = input(color.Color.CYAN + ">>> " + color.Color.END)
            if not prompt:
                continue
            elif prompt.lower() in ["exit", "quit", "bye"]:
                break
            else:
                print(color.Color.CYAN + "ChatGPT is thinking..." + color.Color.END)
                answer = gpt.send(prompt=prompt)
                print(
                    color.Color.GREEN
                    + f"ChatGPT: {answer['reply']}\n"
                    + color.Color.RED
                    + f'(consumed tokens: {answer["consumed_tokens"]})'
                    + color.Color.END
                )
        except Exception as e:
            print(color.Color.REVERCE + color.Color.RED + f"{e}" + color.Color.END)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Config argument to set up ChatGPT")
    parser.add_argument("--gpt4", action="store_true", help="Use GPT-4 or not")
    parser.add_argument(
        "-t", "--timeout", default=30, type=int, help="Timeout until receive response"
    )
    args = parser.parse_args()

    main(args)
