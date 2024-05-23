from pydantic import BaseModel, Field
import uuid


class Reservation(BaseModel):
    reservation_id: str
    listing_id: str
    user_id: str
    start_date: str
    end_date: str
    total_price: float
