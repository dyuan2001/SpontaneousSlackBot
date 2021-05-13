from dotenv import dotenv_values
import pymongo
import ssl

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

client = pymongo.MongoClient("mongodb+srv://admin:" + config["MONGODB_PASSWORD"] + "@cluster0.5mgsb.mongodb.net/MeetingDatabase?retryWrites=true&w=majority",
                            ssl_cert_reqs=ssl.CERT_NONE)
db = client.MeetingDatabase