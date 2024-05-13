import os
import pymongo
from icecream import ic
import pymongo.errors


MONGO_URI = os.environ["MONGO_URI"]
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

connection_string = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{
    MONGO_URI}/?retryWrites=true&w=majority&appName={DB_NAME}"


async def check_connection(client):
    try:
        info = await client.server_info()
        ic(info)
        for key, value in info.item():
            print(f'{key}: {value}')
    except pymongo.errors.ServerSelectionTimeoutError as e:
        print(f"Error: {e}")
    finally:
        await client.close()

db_client = pymongo.MongoClient(connection_string)
check_connection(db_client)
db_client = db_client.get_database(DB_NAME)

user_collection = db_client.get_collection('users')
