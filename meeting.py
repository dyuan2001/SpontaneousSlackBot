from datetime import datetime
from db import db
from db import dbEntry
from slack import client
import uuid

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
def create(ack, say, command, user_store):
    ack()

    participantsRaw = command["text"]
    participants = participantsRaw.split(" ")
    participantIds = []

    participantText = "New meeting request: \n *Participants*: " + participantsRaw

    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": str(uuid.uuid4())
            }
        },
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": participantText
			}
		},
		# {
		# 	"type": "section",
		# 	"fields": [
		# 		{
		# 			"type": "mrkdwn",
		# 			"text": "*Type:*\nComputer (laptop)"
		# 		},
		# 		{
		# 			"type": "mrkdwn",
		# 			"text": "*When:*\nSubmitted Aut 10"
		# 		},
		# 		{
		# 			"type": "mrkdwn",
		# 			"text": "*Last Update:*\nMar 10, 2015 (3 years, 5 months)"
		# 		},
		# 		{
		# 			"type": "mrkdwn",
		# 			"text": "*Reason:*\nAll vowel keys aren't working."
		# 		},
		# 		{
		# 			"type": "mrkdwn",
		# 			"text": "*Specs:*\n\"Cheetah Pro 15\" - Fast, really fast\""
		# 		}
		# 	]
		# },
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Free"
					},
					"style": "primary",
					"value": "click_me_123",
                    "action_id": "approve"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Not Free"
					},
					"style": "danger",
					"value": "click_me_123",
                    "action_id": "deny"
				}
			]
		}
	]

    entry = dbEntry(len(participants))
    collection = db.meeting

    for participant in participants:
        userID = user_store[participant[1:]]["id"]
        participantIds.append(userID)
        entry.add_participant(userID, participant)
        say(blocks=blocks, text=f"You have created it successfully.", channel=userID)
    
    id = blocks[0]['text']['text']
    meeting_dict = entry.get_dict_entry()
    meeting_dict["_id"] = id

    meeting_id = collection.insert_one(meeting_dict).inserted_id
    print(">>>>>>Creating meeting id: " + str(meeting_id))
    # for document in collection.find({}):
    #     if "slackID" not in document.keys():
    #         say("Breakpoint")
    #         post_id = collection.insert_one("PARTICIPANTID").inserted_id #Needs to change
    #         say("Breakpoint")
    #         curr_db_entry = collection.find_one({"id":post_id})
    #         say(text=f"You have created it successfully. Meeting ID:" + post_id)
    print(command)
    
    testDict = {}
    for participantId in participantIds:
        testDict[participantId] = 'hello'
    print(list(testDict))

def approve_meeting(body, ack, say):
    ack()

    print(body)

    id = body['message']['blocks'][0]['text']['text']

	#Database
    collection = db.meeting
    #for document in collection.find({}):
	    #post_id = document.get(id)
    # timestamp = collection.find_one({"_id": id})["timestamp"]
    # client.chat_delete(channel = body["channel_id"], ts = timestamp)

    collection.update_one({"_id": id}, { "$inc": { "count": 1}})
    meetingCheck(id)

    say(f"<@{body['user']['id']}> has approved the meeting!")
    
def meetingCheck(id):
    #dbEntry.incr_participant_count()
    collection = db.meeting
    curr_db_entry = collection.find_one({"_id":id})
    curr_db_participants_dict = curr_db_entry["participants"]

    if curr_db_entry["count"] == curr_db_entry["max_count"]:
        print(">>>>>>Matched!")
        mass_message_approval(curr_db_participants_dict)
        create_dm(curr_db_participants_dict)

def deny_meeting(body, ack, say):
    ack()

    say(f"<@{body['user']['id']}> has denied the meeting.")
"""
React to meeting
Sends update to MongoDB - update map
Checks if all participants have RSVP'd
"""

def mass_message_approval(participant_dict):
    participant_dict_values = participant_dict.values()
    participant_dict_keys = list(participant_dict)

    text = ""
    for participant in participant_dict_values:
        text += participant + ", "

    text = "Your meeting with " + text + "is ready!"

    for participant in participant_dict_keys:
        client.chat_postMessage(
            channel=participant,
            text=text
        )

def create_dm(participant_dict):
    print(">>>>>>Creating dm...")
    response = client.conversations_open(users=list(participant_dict))
    print(response)
    response2 = client.chat_postMessage(
        channel=response['channel']['id'],
        text="Your meeting is ready!"
    )

# def react(body, ack, say):
# 	pass
# 	#say(f"<@{body['user']['id']}> clicked the button")
	
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
