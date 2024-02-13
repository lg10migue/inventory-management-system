from pydantic import BaseModel
from typing import Optional, List


class Supplier(BaseModel):
    name: str
    contact_info: str
    products: List[str]


class SupplierCreate(Supplier):
    id: Optional[str]
