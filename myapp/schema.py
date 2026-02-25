from ninja import Schema
from typing import Optional
from datetime import datetime

class UserCreateSchema(Schema):
    username: str
    password: str

class ProductSchema(Schema):
    id: Optional[int]
    name: str
    description: str
    price: float
    created_at: Optional[datetime]
