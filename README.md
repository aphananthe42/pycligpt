## PyCliGPT

This is a program that allows you to talk to ChatGPT from the terminal.

The model is gpt-3.5-turbo by default, but it can also talk to other models in the configuration.

![screenshot](https://github.com/aphananthe42/pycligpt/blob/main/Assets/Screenshot.png)


## What you need

1. OpenAI API key
   You can get it from the link [here](https://platform.openai.com/account/api-keys).

2. Python3.7 or higher


## Preparation

1. Clone repository from Github.
```shell
$ git clone https://github.com/aphananthe42/pycligpt
```

2. Install dependent libraries from pip.
```shell
$ pip3 install -r requirement.txt
```

3. Make .env file to configure.
```shell
$ cd path/to/pycligpt
$ touch .env
```

```python
# OpenAI API key you get from https://platform.openai.com/account/api-keys
OPENAI_API_KEY = "_YOUR_OPENAI_API_KEY_"

# GPT model you want to use  ex)gpt-3.5-turbo, gpt-4
GPT_MODEL = "gpt-3.5-turbo"

# Time limit for a response to be returned
REQUEST_TIMEOUT = 30
```


## Usage
1. Launch
```shell
$ cd path/to/pycligpt
$ python3 -m pycligpt
```

2. Exit
If you wish to exit, please enter the following words...
"exit", "quit" or "bye"
```shell
>>> exit
```


## License

This project is licensed under the [MIT License](https://github.com/aphananthe42/pycligpt/blob/main/LICENSE).