import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
REQUEST_TIMEOUT = os.environ["REQUEST_TIMEOUT"]
GPT_MODEL = os.environ["GPT_MODEL"]
