from . import chat_gpt, color


def main():
    gpt = chat_gpt.ChatGPT()
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
