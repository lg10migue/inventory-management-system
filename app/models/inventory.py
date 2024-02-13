from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Inventory(BaseModel):
    product_id: str
    type: str
    quantity: int
    date: datetime


class InventoryCreate(Inventory):
    id: Optional[str]
