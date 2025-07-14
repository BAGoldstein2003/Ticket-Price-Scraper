from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def connectToDB():
    load_dotenv('./secrets/secrets.env')
    uri = os.getenv("CONNECTION_STRING")

    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Successfully connected to DB")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    connectToDB()