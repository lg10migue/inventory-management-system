from fastapi import FastAPI
from app.api import product_routes, supplier_routes, inventory_routes
from app.core.firebase import db

app = FastAPI(
    title="Inventory Management API",
    description="A simple inventory management API.",
    version="0.1",
)

app.include_router(product_routes.router)
app.include_router(supplier_routes.router)
app.include_router(inventory_routes.router)


@app.on_event("startup")
def start_firestore_listener():
    product_ref = db.collection("products")
    product_watch = product_ref.on_snapshot(on_snapshot)


def on_snapshot(doc_snapshot, changes, read_time):
    for change in changes:
        if change.type.name == "MODIFIED":
            print("---- Notification received ----")
            print(f"Document has been modified - ID: {change.document.id}")
