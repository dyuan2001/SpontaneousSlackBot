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
    blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "You have a new request:\n*<fakeLink.toEmployeeProfile.com|Fred Enriquez - New device request>*"
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "*Type:*\nComputer (laptop)"
				},
				{
					"type": "mrkdwn",
					"text": "*When:*\nSubmitted Aut 10"
				},
				{
					"type": "mrkdwn",
					"text": "*Last Update:*\nMar 10, 2015 (3 years, 5 months)"
				},
				{
					"type": "mrkdwn",
					"text": "*Reason:*\nAll vowel keys aren't working."
				},
				{
					"type": "mrkdwn",
					"text": "*Specs:*\n\"Cheetah Pro 15\" - Fast, really fast\""
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Approve"
					},
					"style": "primary",
					"value": "click_me_123"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Deny"
					},
					"style": "danger",
					"value": "click_me_123"
				}
			]
		}
	]
    say(blocks=blocks, text=f"You have created it successfully.")
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