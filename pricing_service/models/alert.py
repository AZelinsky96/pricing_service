from uuid import uuid4
from pricing_service.models.item import Item
from pricing_service.common.database import DatabaseLocal as Database


class Alert:

    COLLECTION = "alerts"

    def __init__(self, item_id: str, price_limit: float, _id: str=None)-> None:
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self._id = uuid4() if _id is None else _id

    def to_json(self)-> dict:
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "item_id": self.item_id
        }

    def save_to_mongo(self)-> None:
        Database.insert(self.COLLECTION, self.to_json())

    def load_item_price(self):
        return self.item.load_price()

    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print(f"Item: {self.item} has reduced it's price under {self.price_limit}. Latest price: {self.item.price}")


    def check_and_notify_price(self):
        self.load_item_price()
        self.notify_if_price_reached()


    @classmethod
    def find_all_alerts(cls)-> list:
        alerts_from_db = Database.find_all(cls.COLLECTION, {})
        
        return [cls(**alert) for alert in alerts_from_db]