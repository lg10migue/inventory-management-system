from typing import Dict, Union, List
from app.core.firebase import db


class InventoryCRUD:
    @staticmethod
    def create_inventory_transaction(transaction_data: Dict) -> Union[Dict, None]:
        """Create a new inventory transaction in the Firebase database"""
        try:
            if "product_id" in transaction_data:
                transaction_data["product_id"] = db.collection("products").document(
                    transaction_data["product_id"]
                )
            doc_ref = db.collection("inventory").add(transaction_data)
            transaction_data["id"] = doc_ref[1].id
            transaction_data["product_id"] = transaction_data["product_id"].id
            return transaction_data
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return None

    @staticmethod
    def get_inventory_transaction(transaction_id: str) -> Union[Dict, None]:
        """Get an inventory transaction by its ID from the Firebase database"""
        try:
            doc_ref = db.collection("inventory").document(transaction_id)
            transaction = doc_ref.get()
            if transaction.exists:
                transaction_dic = transaction.to_dict()
                if "product_id" in transaction_dic:
                    transaction_dic["product_id"] = transaction_dic["product_id"].id
                return transaction_dic
            return None
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return None

    @staticmethod
    def update_inventory_transaction(
        transaction_id: str, transaction_data: Dict
    ) -> bool:
        """Update an inventory transaction in the Firebase database"""
        try:
            if "product_id" in transaction_data:
                transaction_data["product_id"] = db.collection("products").document(
                    transaction_data["product_id"]
                )
            db.collection("inventory").document(transaction_id).update(transaction_data)
            return True
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return False

    @staticmethod
    def delete_inventory_transaction(transaction_id: str) -> bool:
        """Delete an inventory transaction from the Firebase database"""
        try:
            db.collection("inventory").document(transaction_id).delete()
            return True
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return False

    @staticmethod
    def get_all_inventory_transaction() -> Union[List[Dict], None]:
        """Get all inventory transactions from the Firebase database"""
        try:
            transactions = db.collection("inventory").stream()
            transactions_list = []
            for transaction in transactions:
                transaction_dic = transaction.to_dict()
                if "product_id" in transaction_dic:
                    transaction_dic["product_id"] = transaction_dic["product_id"].id
                transactions_list.append({"id": transaction.id, **transaction_dic})
            return transactions_list
        except Exception as e:
            print(f"An Error Occurred: {e}")
            return None
