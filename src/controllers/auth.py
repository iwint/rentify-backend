from icecream import ic
from src.services.auth import AuthService


auth_service = AuthService()


class AuthController:
    def __init__(self):
        pass

    def login(self, user: dict):
        ic(user)
        return auth_service.sign_in(user)

    def register(self, user: dict):
        ic(user)
        return auth_service.sign_up(user)

   
