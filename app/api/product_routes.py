from fastapi import APIRouter, HTTPException
from typing import List
from app.models.product import Product, ProductCreate
from app.crud.product_crud import ProductCRUD

router = APIRouter(
    tags=["Products"],
)


@router.post("/product/", response_model=ProductCreate)
async def create_product(product: Product):
    product = product.model_dump(exclude_unset=True)
    new_product = ProductCRUD.create_product(product)
    if new_product:
        return new_product
    raise HTTPException(status_code=500, detail="Product could not be created")


@router.get("/product/{product_id}", response_model=Product)
async def get_product(product_id: str):
    product = ProductCRUD.get_product(product_id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")


@router.put("/product/{product_id}", response_description="Product updated")
async def update_product(product_id: str, product: Product):
    response = ProductCRUD.update_product(
        product_id, product.model_dump(exclude_unset=True)
    )
    if response:
        return {"message": "Product updated successfully"}
    raise HTTPException(status_code=404, detail="Product could not be found or updated")


@router.delete("/product/{product_id}", response_description="Product deleted")
async def delete_product(product_id: str):
    deleted = ProductCRUD.delete_product(product_id)
    if deleted:
        return {"message": "Product deleted"}
    raise HTTPException(
        status_code=404, detail="Product not found or could not be deleted"
    )


@router.get("/products", response_model=List[ProductCreate])
async def get_all_products():
    products = ProductCRUD.get_all_products()
    if products:
        return products
    raise HTTPException(status_code=500, detail="Could not fetch products")
