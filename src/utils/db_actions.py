from datetime import datetime
from src.database.db_connection import collections
from fastapi import HTTPException
from icecream import ic


class DBActions:

    def add_data_to_db(self, collection_name, payload, error_message):
        try:
            payload["created_at"] = datetime.now()
            collections[collection_name].insert_one(payload)
            return payload
        except:
            raise HTTPException(status_code=500, detail=error_message)

    def get_data_from_db(self, collection_name, id_dict, error_message):
        ic(id_dict)
        try:
            data = collections[collection_name].find_one(
                id_dict, {"_id": 0})
            ic(data)
            return data
        except:
            raise HTTPException(status_code=500, detail=error_message)

    def get_all_data_from_db(self, collection_name, id_dict, error_message):
        try:
            if data := collections[collection_name].find(id_dict if id_dict else {}, {"_id": 0}):
                data = [i for i in data]
            return data

        except:
            raise HTTPException(status_code=500, detail=error_message)

    def update_data_in_db(self, collection_name, id_dict, payload, error_message):
        try:
            payload['updated_at'] = datetime.now()
            collections[collection_name].update_one(id_dict, {"$set": payload})
            return True
        except:
            raise HTTPException(status_code=500, detail=error_message)

    def delete_data_from_db(self, collection_name, id_dict, error_message):
        try:
            collections[collection_name].delete_one(id_dict)
            return True
        except:
            raise HTTPException(status_code=500, detail=error_message)
