from pydantic import BaseModel, Field
import uuid


class Reservation(BaseModel):
    reservation_id: str = Field(default_factory=uuid.uuid4, alias="_id")
    listing_id: str = Field(...)
    user_id: str = Field(...)
    start_date: str = Field(...)
    end_date: str = Field(...)
    total_price: float = Field(...)
    created_at: str = Field(...)
