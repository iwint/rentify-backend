from pydantic import BaseModel, Field
import uuid
from typing import List, Optional, Dict


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
