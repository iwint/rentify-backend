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

connection_string = "mongodb://localhost:27017/"


def check_server_connection(client):
    try:
        server_info = client.server_info()
        print("Server Information:")
        for key, value in server_info.items():
            print(f"{key}: {value}")
    except pymongo.errors.ServerSelectionTimeoutError as e:
        ic("Server is down or unreachable")
    finally:
        client.close()


ic(connection_string)

db_client = pymongo.MongoClient(connection_string)
check_server_connection(db_client)
db_client = db_client.get_database(DB_NAME)

user_collection = db_client.get_collection('users')
listing_collection = db_client.get_collection('listings')
reservation_collection = db_client.get_collection('reservations')

collections = {
    "users": user_collection,
    "listings": listing_collection,
    "reservations": reservation_collection
}
