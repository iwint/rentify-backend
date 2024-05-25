import os
import pymongo
from icecream import ic
import pymongo.errors


MONGO_URI = os.environ["MONGO_URI"]
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# connection_string = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{
#     MONGO_URI}/?retryWrites=true&w=majority&appName={DB_NAME}"

connection_string = MONGO_URI


def check_server_connection(client):
    try:
        client.server_info()
    except pymongo.errors.ServerSelectionTimeoutError as e:
        print("Failed to retrieve server information. MongoDB connection may not be alive.")
    finally:
        client.close()


db_client = pymongo.MongoClient(connection_string)
check_server_connection(db_client)
ic(DB_NAME)
db_client = db_client.get_database(DB_NAME)

user_collection = db_client.get_collection('users')
listing_collection = db_client.get_collection('listings')
reservation_collection = db_client.get_collection('reservations')

collections = {
    "users": user_collection,
    "listings": listing_collection,
    "reservations": reservation_collection
}
