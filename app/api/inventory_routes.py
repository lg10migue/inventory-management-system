from fastapi import APIRouter, HTTPException
from typing import List
from app.models.inventory import Inventory, InventoryCreate
from app.crud.inventory_crud import InventoryCRUD

router = APIRouter(
    tags=["Inventory Transactions"],
)


@router.post("/inventory/", response_model=InventoryCreate)
async def create_inventory_transaction(inventory: Inventory):
    inventory = inventory.model_dump(exclude_unset=True)
    new_inventory = InventoryCRUD.create_inventory_transaction(inventory)
    if new_inventory:
        return new_inventory
    raise HTTPException(
        status_code=500, detail="Inventory transaction could not be created"
    )


@router.get("/inventory/{inventory_id}", response_model=Inventory)
async def get_inventory_transaction(inventory_id: str):
    inventory = InventoryCRUD.get_inventory_transaction(inventory_id)
    if inventory:
        return inventory
    raise HTTPException(status_code=404, detail="Inventory transaction not found")


@router.put(
    "/inventory/{inventory_id}", response_description="Inventory transaction updated"
)
async def update_inventory_transaction(inventory_id: str, inventory: Inventory):
    response = InventoryCRUD.update_inventory_transaction(
        inventory_id, inventory.model_dump(exclude_unset=True)
    )
    if response:
        return {"message": "Inventory transaction updated successfully"}
    raise HTTPException(
        status_code=404, detail="Inventory transaction could not be found or updated"
    )


@router.delete(
    "/inventory/{inventory_id}", response_description="Inventory transaction deleted"
)
async def delete_inventory_transaction(inventory_id: str):
    deleted = InventoryCRUD.delete_inventory_transaction(inventory_id)
    if deleted:
        return {"message": "Inventory transaction deleted"}
    raise HTTPException(
        status_code=404,
        detail="Inventory transaction not found or could not be deleted",
    )


@router.get("/inventory_all", response_model=List[InventoryCreate])
async def get_all_inventory_transactions():
    inventory_transactions = InventoryCRUD.get_all_inventory_transaction()
    if inventory_transactions:
        return inventory_transactions
    raise HTTPException(
        status_code=500, detail="Could not fetch inventory transactions"
    )
