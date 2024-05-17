from src.services.reservation import ReservationService

reservation_service = ReservationService()


class ReservationController:
    def create_reservation(self, reservation, user_id):
        return reservation_service.create_reservation(reservation, user_id)
