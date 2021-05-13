import os
from dotenv import dotenv_values
from slack_bolt import App

config = dotenv_values(".env")

# Initializes your app with your bot token and signing secret
app = App(
    token=config["BOT_TOKEN"],
    signing_secret=config["SIGNING_SECRET"]
)

# Listens to incoming messages that contain "hello"
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")

############################################
#Waits for a /setup command and sends a message to be reacted to
@app.command("!setup")
def individual_setup(message, say):
    #ack()
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )

@app.action("button_click")
def react_button(body, ack, say):
    ack()
    say(f"<@{body['user']['id']}> clicked the button")
####################################################

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))