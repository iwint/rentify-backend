import uuid
from pydantic import BaseModel, Field
from typing import List, Optional


class SignInRequest(BaseModel):
    email: str = Field(...)
    password: str = Field(...)


class SignUpRequest(SignInRequest):
    name: str = Field(...)


class AuthResponse(BaseModel):
    token: str = Field(...)
    user_id: str = Field(default_factory=uuid.uuid4, alias="user_id")
    name: str = Field(...)
    email: str = Field(...)
    reservations: List = Field(...),
    listings: List = Field(...),
    favorite_ids: List = Field(...),
    accounts: List = Field(...),
