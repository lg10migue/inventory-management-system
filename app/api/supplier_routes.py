from fastapi import APIRouter, HTTPException
from typing import List
from app.models.supplier import Supplier, SupplierCreate
from app.crud.supplier_crud import SupplierCRUD

router = APIRouter(
    tags=["Suppliers"],
)


@router.post("/supplier/", response_model=SupplierCreate)
async def create_supplier(supplier: Supplier):
    supplier = supplier.model_dump(exclude_unset=True)
    new_supplier = SupplierCRUD.create_supplier(supplier)
    if new_supplier:
        return new_supplier
    raise HTTPException(status_code=500, detail="Supplier could not be created")


@router.get("/supplier/{supplier_id}", response_model=Supplier)
async def get_supplier(supplier_id: str):
    supplier = SupplierCRUD.get_supplier(supplier_id)
    if supplier:
        return supplier
    raise HTTPException(status_code=404, detail="Supplier not found")


@router.put("/supplier/{supplier_id}", response_description="Supplier updated")
async def update_supplier(supplier_id: str, supplier: Supplier):
    response = SupplierCRUD.update_supplier(
        supplier_id, supplier.model_dump(exclude_unset=True)
    )
    if response:
        return {"message": "Supplier updated successfully"}
    raise HTTPException(
        status_code=404, detail="Supplier could not be found or updated"
    )


@router.delete("/supplier/{supplier_id}", response_description="Supplier deleted")
async def delete_supplier(supplier_id: str):
    deleted = SupplierCRUD.delete_supplier(supplier_id)
    if deleted:
        return {"message": "Supplier deleted"}
    raise HTTPException(
        status_code=404, detail="Supplier not found or could not be deleted"
    )


@router.get("/suppliers", response_model=List[SupplierCreate])
async def get_all_suppliers():
    suppliers = SupplierCRUD.get_all_suppliers()
    if suppliers:
        return suppliers
    raise HTTPException(status_code=500, detail="Could not fetch suppliers")
