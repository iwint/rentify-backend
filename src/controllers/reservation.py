from src.services.reservation import ReservationService

reservation_service = ReservationService()


class ReservationController:
    def create_reservation(self, reservation, user_id):
        return reservation_service.create_reservation(reservation, user_id)

    def get_reservation(self, id, by):
        return reservation_service.get_reservation_by_id(id, by)

    def get_all_reservations(self):
        return reservation_service.get_all_reservations()

    def delete_reservation(self, reservation_id):
        return reservation_service.delete_reservation(reservation_id)
