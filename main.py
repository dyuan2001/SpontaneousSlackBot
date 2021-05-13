from dotenv import dotenv_values
import pymongo
import ssl
# import asyncio

import os
from dotenv import dotenv_values
from slack_bolt import App

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

client = pymongo.MongoClient("mongodb+srv://admin:" + config["MONGODB_PASSWORD"] + "@cluster0.5mgsb.mongodb.net/MeetingDatabase?retryWrites=true&w=majority",
                            ssl_cert_reqs=ssl.CERT_NONE)
db = client.MeetingDatabase

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
    say(text=f"Hey there <@{message['user']}>!")

from meeting import pingpong

@app.message('!ping')
def message_pingpong(message, say):
    pingpong(message, say)

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
    print("This is working")

# async def test():
obj = db.meeting.find()
print(obj)
for o in obj:
    print(o['_id'])
obj2 = db.meeting.find_one()
print(obj2)

# asyncio.run(test())