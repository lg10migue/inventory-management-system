from typing import Dict, Union, List
from app.core.firebase import db


class ProductCRUD:
    @staticmethod
    def create_product(product_data: Dict) -> Union[Dict, None]:
        """Create a new product in the Firebase database"""
        try:
            doc_ref = db.collection("products").add(product_data)
            product_data["id"] = doc_ref[1].id
            return product_data
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return None

    @staticmethod
    def get_product(product_id: str) -> Union[Dict, None]:
        """Get a product by its ID from the Firebase database"""
        try:
            doc_ref = db.collection("products").document(product_id)
            product = doc_ref.get()
            if product.exists:
                return product.to_dict()
            return None
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return None

    @staticmethod
    def update_product(product_id: str, product_data: Dict) -> bool:
        """Update a product in the Firebase database"""
        try:
            db.collection("products").document(product_id).update(product_data)
            return True
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return False

    @staticmethod
    def delete_product(product_id: str) -> bool:
        """Delete a product from the Firebase database"""
        try:
            db.collection("products").document(product_id).delete()
            return True
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return False

    @staticmethod
    def get_all_products() -> Union[List[Dict], None]:
        """Get all products from the Firebase database"""
        try:
            products = db.collection("products").stream()
            return [{"id": product.id, **product.to_dict()} for product in products]
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return None
