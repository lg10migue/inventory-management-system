from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class ProductCreate(Product):
    id: Optional[str]
