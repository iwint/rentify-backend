from src.utils.db_actions import DBActions
from fastapi import HTTPException
from icecream import ic
import uuid

db_actions = DBActions()


class ReservationService:

    def create_reservation(self, reservation, email):
        ic(reservation, email)
        if reservation and email:
            user = db_actions.get_data_from_db(
                'users', {"email": email}, "Error retrieving user")
            listing = db_actions.get_data_from_db(
                'listings', {'listing_id': reservation['listing_id']}, "Error retrieving listing")
            reservation["user_id"] = user['user_id']
            reservation['listing'] = listing
            reservation['author'] = listing['user_id']
            reservation["reservation_id"] = str(uuid.uuid4())
            user['reservations'].append(reservation)
            added_reservation = db_actions.add_data_to_db(
                "reservations", reservation, "Error creating reservation")
            return added_reservation
        else:
            raise HTTPException(
                status_code=400, detail="Invalid reservation data")

    def get_reservation_by_id(self, id, by):
        ic(id, by)
        if by == "listing":
            reservation = db_actions.get_all_data_from_db(
                'reservations', {"listing_id": id}, "Error retrieving reservation")
            return reservation
        elif by == "user":
            return db_actions.get_all_data_from_db('reservations', {"user_id": id}, "Error retrieving reservation")
        elif by == "author":
            return db_actions.get_all_data_from_db('reservations', {"author": id}, "Error retrieving reservation")
        else:
            raise HTTPException(
                status_code=400, detail="Invalid search criteria")

    def get_all_reservations(self):
        return db_actions.get_all_data_from_db('reservations', "Error retrieving reservations")

    def delete_reservation(self, reservation_id):
        return db_actions.delete_data_from_db('reservations', {"reservation_id": reservation_id}, "Error deleting reservation")
