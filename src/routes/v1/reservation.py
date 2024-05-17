from fastapi import APIRouter, status, Body, Depends
from src.utils.jwt import AuthHandler
from src.models.reservation import Reservation
from src.controllers.reservation import ReservationController

router = APIRouter()
auth_handler = AuthHandler()
reservation_controller = ReservationController()


@router.post("/", response_model=Reservation, response_description="Create a new reservation", status_code=status.HTTP_201_CREATED)
def create_reservation(reservation=Body(...), user_id=Depends(auth_handler.auth_wrapper)):
    return reservation_controller.create_reservation(reservation, user_id)
