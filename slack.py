from slack_sdk import WebClient
from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

client = WebClient(token=config["BOT_TOKEN"])