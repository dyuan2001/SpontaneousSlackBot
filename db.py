from dotenv import dotenv_values
import pymongo
import ssl

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

client = pymongo.MongoClient("mongodb+srv://admin:" + config["MONGODB_PASSWORD"] + "@cluster0.5mgsb.mongodb.net/MeetingDatabase?retryWrites=true&w=majority",
                            ssl_cert_reqs=ssl.CERT_NONE)
db = client.MeetingDatabase

class dbEntry():
    
    def __init__(self, participant_count):
        self.max_count = participant_count
        self.participant_count = 0
        self.everyone_is_ready = False;
        self.dict_entry = {}
        self.dict_entry["count"] = 0
        self.dict_entry["max_count"] = participant_count
        self.dict_entry["participants"] = {}
        # self.dict_entry["timestamp"] = timestamp

    def incr_participant_count(self):
        self.participantCount += 1

    def decr_participant_count(self):
        if self.participantCount > 0:
            self.participantCount -= 1
    
    def add_participant(self, userID, name):
        self.dict_entry["participants"][userID] = name

    def is_full(self):
        if self.max_count == self.participant_count:
            return True
        return False

    def get_participant_count(self):
        return self.participant_count
    
    def get_max_count(self):
        return self.max_count

    def get_dict_entry(self):
        return self.dict_entry

def get_db_entry(id):
    return db.meeting.find({"_id": id})