from src.utils.db_actions import DBActions
from fastapi import HTTPException


db_actions = DBActions()


class ReservationService:

    def create_reservation(self, reservation, user_id):
        if reservation and user_id:
            reservation["user_id"] = user_id
            return db_actions.add_data_to_db("reservations", reservation, "Error creating reservation")
        else:
            raise HTTPException(
                status_code=400, detail="Invalid reservation data")
        