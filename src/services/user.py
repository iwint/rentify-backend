from icecream import ic
from src.database.db_connection import user_collection
from fastapi import HTTPException, status
from src.utils.db_actions import DBActions


db_actions = DBActions()


class UserService:

    def get_user(self, email):
        if user := user_collection.find_one({"email": email}):
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")

    def update_favourite_id(self, email, listing_id):
        existing_favorite_ids = user_collection.find_one({"email": email})[
            "favorite_ids"]
        ic(existing_favorite_ids)

        if listing_id is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Listing ID cannot be None")
        elif listing_id in existing_favorite_ids:
            existing_favorite_ids.remove(listing_id)
            user_collection.update_one(
                {"email": email}, {"$set": {"favorite_ids": existing_favorite_ids}})
            return {"message": "Listing removed from favorites"}
        else:
            existing_favorite_ids.append(listing_id)
            user_collection.update_one(
                {"email": email}, {"$push": {"favorite_ids": listing_id}})
            return {"message": "Listing added to favorites"}

    def get_all_favourites(self, email):
        user = user_collection.find_one({"email": email})
        if user:
            favourite_ids = user['favorite_ids']
            favourites = []

            for id in favourite_ids:

                listing = db_actions.get_data_from_db(
                    'listings', {'listing_id': id}, 'Error in getting favourites')
                favourites.append(listing)

            return favourites
        else:
            raise HTTPException(
                status_code='404', detail='User not found')

    def get_all_properties(self, email):
        user = user_collection.find_one({"email": email})
        if user:
            properties = []
            listings = db_actions.get_all_data_from_db(
                'listings', {'user_id': user['user_id']}, 'Error in getting properties')

            return listings
        else:
            raise HTTPException(
                status_code='404', detail='User not found')
