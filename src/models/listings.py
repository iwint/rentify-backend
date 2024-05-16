import uuid
from typing import Dict
from pydantic import BaseModel, Field


class Listing(BaseModel):
    listing_id: str = Field(default_factory=uuid.uuid4, alias="listing_id",)
    category: str = Field(...)
    location: Dict = Field(...)
    guest_count: int = Field(...)
    room_count: int = Field(...)
    bathroom_count: int = Field(...)
    image_src: str = Field(...)
    price: str = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    user_id: str = Field(...)


class ListingUserDetails(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    user_id: str = Field(...)


class SingleListingResponse(Listing):
    user: ListingUserDetails = Field(...)
