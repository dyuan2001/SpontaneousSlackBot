from db import db


def pingpong(message, say):
    say(text=f"Pong <@{message['user']}>!")
    print(message)

"""
Create meeting
/create meeting int:timeout list:<participants>
Sends meeting to MongoDB - timeout + map<participant, <message_id, bool>>
dict(participants), participants(message_id, bool)
Sends notification to each participant w/ react message
"""
def create(ack, say, command):
    ack()
    say(text=f"You have created it successfully.")
    print(command)


"""
React to meeting
Sends update to MongoDB - update map
Checks if all participants have RSVP'd
"""

"""
Set up meeting
Creates a new Group DM with all participants
Deletes MongoDB entry
"""

"""
Delete meeting
Sends update to MongoDB - delete entry
Change message for all Slack users
"""