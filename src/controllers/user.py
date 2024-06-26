from src.services.user import UserService

user_service = UserService()


class UserController:

    def get_user(self, user_id: str):
        return user_service.get_user(user_id)

    def update_favorite_id(self, user_id: str, listing_id: str):
        return user_service.update_favourite_id(user_id, listing_id)

    def get_all_favourites(self, email):
        return user_service.get_all_favourites(email)

    def get_all_properties(self, email):
        return user_service.get_all_properties(email)
