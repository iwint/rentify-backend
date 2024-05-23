import uuid
from typing import Dict
from pydantic import BaseModel, Field


class Listing(BaseModel):
    listing_id: str
    category: str
    location: Dict
    guest_count: int
    room_count: int
    bathroom_count: int
    image_src: str
    price: str
    title: str
    description: str
    user_id: str


class ListingUserDetails(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    user_id: str = Field(...)


class SingleListingResponse(Listing):
    user: ListingUserDetails = Field(...)
