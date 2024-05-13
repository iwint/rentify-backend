from typing import Dict
from fastapi import APIRouter, status
from src.controllers.auth import AuthController
from src.models.auth import AuthResponse, SignInRequest, SignUpRequest


router = APIRouter()
auth_controller = AuthController()


@router.post("/sign-in", response_description="Sign in", status_code=status.HTTP_200_OK, response_model=AuthResponse)
async def sign_in(User: SignInRequest):
    user = User.dict()
    return auth_controller.login(user=user)


@router.post("/register", response_description="Register", status_code=status.HTTP_201_CREATED, response_model=AuthResponse)
async def register(User: SignUpRequest):
    user = User.dict()
    return auth_controller.register(user=user)
