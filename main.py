from dotenv import dotenv_values
import pymongo

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

client = pymongo.MongoClient("mongodb+srv://admin:" + config["MONGODB_PASSWORD"] + "@cluster0.5mgsb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test