from src.utils.db_actions import DBActions
from fastapi import HTTPException
from icecream import ic
import uuid

db_actions = DBActions()


class ReservationService:

    def create_reservation(self, reservation, user_id):
        ic(reservation, user_id)
        if reservation and user_id:
            reservation["user_id"] = user_id
            reservation["reservation_id"] = str(uuid.uuid4())
            user = db_actions.get_data_from_db(
                'users', {"email": user_id}, "Error retrieving user")
            user['reservations'].append(reservation)
            db_actions.update_data_in_db(
                'users', {"user_id": user_id}, user, "Error updating user")
            added_reservation = db_actions.add_data_to_db(
                "reservations", reservation, "Error creating reservation")
            return added_reservation
        else:
            raise HTTPException(
                status_code=400, detail="Invalid reservation data")
