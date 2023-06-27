from enum import Enum


class Prompt(Enum):
    to_english = "You are an excellent translator. Please translate all the sentences given henceforth into English."
    to_japanese = "You are an excellent translator. Please translate all the sentences given henceforth into Japanese."
    default = "You are a helpful assistant."
