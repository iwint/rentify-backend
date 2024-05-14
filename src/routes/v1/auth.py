from typing import Dict
from fastapi import APIRouter, status, Depends
from src.controllers.auth import AuthController
from src.models.auth import AuthResponse, SignInRequest, SignUpRequest
from src.utils.jwt import AuthHandler

router = APIRouter()
auth_controller = AuthController()
auth_handler = AuthHandler()


@router.post("/sign-in", response_description="Sign in", status_code=status.HTTP_200_OK, response_model=AuthResponse)
async def sign_in(User: SignInRequest):
    user = User.dict()
    return auth_controller.login(user=user)


@router.post("/register", response_description="Register", status_code=status.HTTP_201_CREATED, response_model=AuthResponse)
async def register(User: SignUpRequest):
    user = User.dict()
    return auth_controller.register(user=user)


@router.get("/user", response_description="Get user", status_code=status.HTTP_200_OK, response_model=AuthResponse)
async def get_user(user_id=Depends(auth_handler.auth_wrapper)):
    return auth_controller.get_user(user_id=user_id)
