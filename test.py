import os
from dotenv import dotenv_values
from slack_bolt import App

config = dotenv_values(".env")

# Initializes your app with your bot token and signing secret
app = App(
    token=config["BOT_TOKEN"],
    signing_secret=config["SIGNING_SECRET"]
)

print("Test log")

# Listens to incoming messages that contain "hello"
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
    print("This is working")