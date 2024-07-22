import argparse

from . import chat_gpt, color


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-en", "--english", action="store_true")
    group.add_argument("-ja", "--japanese", action="store_true")
    args = parser.parse_args()

    gpt = chat_gpt.ChatGPT(to_english=args.english, to_japanese=args.japanese)
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
        except KeyboardInterrupt:
            print(color.Color.REVERCE + color.Color.RED + "Keyboard interrupt" + color.Color.END)
        except Exception as e:
            print(color.Color.REVERCE + color.Color.RED + f"{e}" + color.Color.END)
