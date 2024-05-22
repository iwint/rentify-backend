from fastapi import APIRouter, status, Body, Depends
from src.utils.jwt import AuthHandler
from src.models.reservation import Reservation
from src.controllers.reservation import ReservationController
from icecream import ic


router = APIRouter()
auth_handler = AuthHandler()
reservation_controller = ReservationController()


@router.post("/", response_model=Reservation, response_description="Create a new reservation", status_code=status.HTTP_201_CREATED)
def create_reservation(reservation=Body(...), user_id=Depends(auth_handler.auth_wrapper)):
    return reservation_controller.create_reservation(reservation, user_id)


@router.get("/{by}/{id}", response_description="Get a reservation", status_code=status.HTTP_200_OK)
def get_reservation(id: str, by: str):
    return reservation_controller.get_reservation(id, by)


@router.get("/", response_description="Get all reservations", status_code=status.HTTP_200_OK)
def get_all_reservations():
    return reservation_controller.get_all_reservations()


@router.delete("/{reservation_id}", response_description="Delete a reservation", status_code=status.HTTP_200_OK)
def delete_reservation(reservation_id: str, user_id=Depends(auth_handler.auth_wrapper)):
    return reservation_controller.delete_reservation(reservation_id)
