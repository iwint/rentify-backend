from fastapi import APIRouter, Depends, status
from src.models.auth import AuthResponse
from src.controllers.user import UserController
from src.utils.jwt import AuthHandler


router = APIRouter()
auth_handler = AuthHandler()
user_controller = UserController()


@router.get("/", response_description="Get user", status_code=status.HTTP_200_OK, response_model=AuthResponse)
async def get_user(user_id=Depends(auth_handler.auth_wrapper)):
    return user_controller.get_user(user_id=user_id)


@router.put("/favorite/{listing_id}", response_description="Update favorite", status_code=status.HTTP_200_OK)
async def update_favorite(listing_id: str, user_id=Depends(auth_handler.auth_wrapper)):
    return user_controller.update_favorite_id(user_id=user_id, listing_id=listing_id)


@router.get('/favourites', response_description="Get all favourite listings", status_code=status.HTTP_200_OK)
async def get_all_favourites(email=Depends(auth_handler.auth_wrapper)):
    return user_controller.get_all_favourites(email)


@router.get('/properties', response_description="Get all favourite listings", status_code=status.HTTP_200_OK)
async def get_all_properties(email=Depends(auth_handler.auth_wrapper)):
    return user_controller.get_all_properties(email)
