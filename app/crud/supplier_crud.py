from typing import Dict, Union, List
from app.core.firebase import db


class SupplierCRUD:
    @staticmethod
    def create_supplier(supplier_data: Dict) -> Union[Dict, None]:
        """Create a new supplier in the Firebase database"""
        try:
            if "products" in supplier_data:
                supplier_data["products"] = [
                    db.collection("products").document(product_id)
                    for product_id in supplier_data["products"]
                ]
            doc_ref = db.collection("suppliers").add(supplier_data)
            supplier_data["id"] = doc_ref[1].id

            # Convert DocumentReference to ID.
            supplier_data["products"] = [
                product_ref.id for product_ref in supplier_data["products"]
            ]
            return supplier_data
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return None

    @staticmethod
    def get_supplier(supplier_id: str) -> Union[Dict, None]:
        """Get a supplier by its ID from the Firebase database"""
        try:
            doc_ref = db.collection("suppliers").document(supplier_id)
            supplier = doc_ref.get()
            if supplier.exists:
                supplier_dict = supplier.to_dict()
                if "products" in supplier_dict:
                    supplier_dict["products"] = [
                        product_ref.id for product_ref in supplier_dict["products"]
                    ]
                return supplier_dict
            return None
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return None

    @staticmethod
    def update_supplier(supplier_id: str, supplier_data: Dict) -> bool:
        """Update a supplier in the Firebase database"""
        try:
            if "products" in supplier_data:
                supplier_data["products"] = [
                    db.collection("products").document(product_id)
                    for product_id in supplier_data["products"]
                ]
            db.collection("suppliers").document(supplier_id).update(supplier_data)
            return True
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return False

    @staticmethod
    def delete_supplier(supplier_id: str) -> bool:
        """Delete a supplier from the Firebase database"""
        try:
            db.collection("suppliers").document(supplier_id).delete()
            return True
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return False

    @staticmethod
    def get_all_suppliers() -> Union[List[Dict], None]:
        """Get all suppliers from the Firebase database"""
        try:
            suppliers = db.collection("suppliers").stream()
            suppliers_list = []
            for sup in suppliers:
                supplier = sup.to_dict()
                if "products" in supplier:
                    supplier["products"] = [
                        product_ref.id for product_ref in supplier["products"]
                    ]
                suppliers_list.append({"id": sup.id, **supplier})
            return suppliers_list
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return None
