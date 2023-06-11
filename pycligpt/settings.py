import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
GPT_MODEL = os.environ.get("GPT_MODEL", "gpt-3.5-turbo")
REQUEST_TIMEOUT = os.environ.get("REQUEST_TIMEOUT", 30)
