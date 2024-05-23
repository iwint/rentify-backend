import uuid
from typing import List

from pydantic import BaseModel


class SignInRequest(BaseModel):
    email: str
    password: str


class SignUpRequest(SignInRequest):
    name: str
    role: str


class AuthResponse(BaseModel):
    token: str
    user_id: str
    name: str
    email: str
    reservations: List
    listings: List
    favorite_ids: List
    accounts: List
    role: str
