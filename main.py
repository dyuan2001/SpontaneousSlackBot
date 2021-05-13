from dotenv import dotenv_values
import pymongo
# import asyncio
from time import time

import os
from slack_bolt import App
from slack_sdk import WebClient
import meeting
from slack import client

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

# You probably want to use a database to store any user information ;)
users_store = {}

# Put users into the dict
def save_users(users_array):
    for user in users_array:
        # Key user info on their unique user ID
        user_name = user["name"]
        # Store the entire user object (you may not need all of the info)
        users_store[user_name] = user

# Call the users.list method using the WebClient
# users.list requires the users:read scope
result = client.users_list()
save_users(result["members"])


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


@app.message('!ping')
def message_pingpong(message, say):
    meeting.pingpong(message, say)

@app.command("/createmeeting")
def createMeeting(ack, say, command):
    meeting.create(ack, say, command, users_store)

@app.action("approve")
def approve_request(body, ack, say):
    meeting.approve_meeting(body, ack, say)

@app.action("deny")
def deny_request(body, ack, say):
    meeting.deny_meeting(body, ack, say)

@app.command("/createChannel")
def createChannel(ack, say, command):
    ack()
    channel_name = f"my-private-channel"
    response = client.conversations_create(
    name=channel_name,
    is_private=True
    )
    channel_id = response["channel"]["id"]
    response = client.conversations_archive(channel=channel_id)
    say(text=f'channel has been created.')


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