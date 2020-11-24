import re

from uuid import uuid4

from pricing_service.models.model import Model


class Store(Model):
    collection = "stores"

    def __init__(self, name: str, url_prefix: str, tag_name: str, query: dict, _id: str=None)-> None:
        super().__init__()
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = _id or uuid4().hex

    def to_json(self)-> dict:
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }
    
    @classmethod
    def get_by_name(cls, store_name: str)-> cls:
        return cls.find_by_one(attribute="name", value=store_name)
    
    @classmethod
    def get_by_url_prefix(cls, url_prefix: str)-> cls:
        url_regex = {"$regex": f"^{url_prefix}"}
        return cls.find_by_one(attibute="url_prefix", value=url_regex)

    @classmethod
    def find_by_url(cls, url: str)-> cls:
        pattern = re.compile(r"https?://.*?/")
        return cls.get_by_url_prefix(pattern.search(url).group(1))
