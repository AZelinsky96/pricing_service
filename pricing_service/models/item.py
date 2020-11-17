from uuid import uuid4
from pricing_service.common.common import get_content
from pricing_service.models.model import Model
from pricing_service.common.parsers import PriceParser
from pricing_service.common.database import DatabaseLocal as Database


class Item(Model):
    
    COLLECTION = "items"

    def __init__(self, url: str, tag_name: str, query: dict, _id: str=None)-> None:
        super().__init__()
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None
        self._id = uuid4().hex if _id is None else _id

    def __repr__(self)-> str:
        return f"<item {self.url}>"

    def load_price(self)-> float:
        content = get_content(self.url)
        self.price = PriceParser(content, "html").get_price(self.tag_name, self.query)
        return self.price
    
    def to_json(self)-> dict:
        return {
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "query": self.query
        }
