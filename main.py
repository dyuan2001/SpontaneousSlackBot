from dotenv import dotenv_values
import pymongo
# import asyncio

import os
from slack_bolt import App

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

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


""" 
INDIVIDUAL MEETINGS
"""
import meeting

@app.message('!ping')
def message_pingpong(message, say):
    meeting.pingpong(message, say)

@app.command("/createmeeting")
def createMeeting(ack, say, command):
    meeting.create(ack, say, command)





# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
    print("This is working")




# # async def test():
# obj = db.meeting.find()
# print(obj)
# for o in obj:
#     print(o['_id'])
# obj2 = db.meeting.find_one()
# print(obj2)

# # asyncio.run(test())