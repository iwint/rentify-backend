from fastapi import APIRouter, Depends, Body, status
from src.utils.jwt import AuthHandler
from src.models.listings import Listing, SingleListingResponse
from src.controllers.listings import ListingController
from icecream import ic

router = APIRouter()
auth_handler = AuthHandler()
listing_controller = ListingController()


@router.post("/", response_model=Listing, response_description="Create a new listing", status_code=201)
def create_listing(listing=Body(...), user_id=Depends(auth_handler.auth_wrapper)):
    return listing_controller.create_listing(listing)


@router.get("/",  response_description="Get all listings", status_code=200)
def get_all_listings():
    return listing_controller.get_all_listings()


@router.get("/{listing_id}", response_description="Get a listing by id", status_code=status.HTTP_200_OK, response_model=SingleListingResponse)
def get_listing_by_id(listing_id: str):
    ic(listing_id)
    return listing_controller.get_listing_by_id(listing_id)
