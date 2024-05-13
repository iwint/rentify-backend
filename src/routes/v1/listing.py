from fastapi import APIRouter, Depends, Body
from src.utils.jwt import AuthHandler
from src.models.listing import Listing
from src.controllers.listing import ListingController
from icecream import ic

router = APIRouter()
auth_handler = AuthHandler()
listing_controller = ListingController()


@router.post("/")
async def create_listing(listing: Listing = Body(...), user_id=Depends(auth_handler.auth_wrapper)):
    ic(user_id)
    return listing_controller.create_listing(listing)
