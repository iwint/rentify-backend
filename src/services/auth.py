from src.database.db_connection import user_collection
from fastapi import HTTPException
from src.utils.jwt import AuthHandler
from icecream import ic
from src.utils.bcrypt import PasswordHandler
import uuid

auth_handler = AuthHandler()
password_handler = PasswordHandler()


class AuthService:
    def sign_in(self, user):
        registered_user = user_collection.find_one({"email": user['email']})
        ic(registered_user)
        if registered_user:
            is_verified = password_handler.check_password(
                user['password'], registered_user['password'])

        try:
            if (registered_user and is_verified):
                return {
                    "user_id": str(registered_user['_id']),
                    "name": registered_user['name'],
                    "email": registered_user['email'],
                    "reservations": registered_user['reservations'],
                    "listings": registered_user['listings'],
                    "favorite_ids": registered_user['favorite_ids'],
                    "accounts": registered_user['accounts'],
                    "token": registered_user['token'],
                    "role": registered_user['role']
                }
            else:
                raise HTTPException(
                    status_code=401, detail="Invalid email or password")
        except KeyError:
            raise HTTPException(
                status_code=401, detail="Invalid email or password")

    def sign_up(self, user):
        ic(user)
        is_registered = user_collection.find_one({"email": user['email']})
        try:
            if is_registered:
                raise HTTPException(
                    status_code=400, detail="User already exists")
            else:
                hashed_password = password_handler.get_password_hash(
                    user['password'])
                user_details = {}
                user_id = str(uuid.uuid4())
                user_details['user_id'] = user_id
                user_details['name'] = user['name']
                user_details['email'] = user['email']
                user_details['role'] = user['role']
                user_details['password'] = hashed_password
                user_details['reservations'] = []
                user_details['listings'] = []
                user_details['favorite_ids'] = []
                user_details['accounts'] = []
                user_details['token'] = auth_handler.encode_token(
                    user['email'])
                user_collection.insert_one(user_details)
                return user_details
        except KeyError:
            raise HTTPException(
                status_code=400, detail="Invalid email or password")

    def get_user(self, user_id):
        ic(user_id)
        user = user_collection.find_one({"email": user_id})
        ic(user)
        return user
