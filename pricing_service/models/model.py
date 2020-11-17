from abc import ABCMeta, abstractmethod
from pricing_service.common.database import Database
from typing import TypeVar, Type, List


T = TypeVar("T", bound="Model")


class Model(metaclass=ABCMeta):
    
    COLLECTION: str
    _id: str

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def to_json(self)-> dict:
        raise NotImplementedError

    def save_to_mongo(self)-> None:
        Database.update(self.COLLECTION, {"_id": self._id}, self.to_json())
    
    def remove_from_mongo(self)-> None:
        Database.remove(self.COLLECTION, {"_id": self._id})

    @classmethod
    def find_all_elements(cls: Type[T])-> List[T]:
        elements_from_db = Database.find_all(cls.COLLECTION, {})
        return [cls(**element) for element in elements_from_db]

    @classmethod
    def find_by_one(cls: Type[T], attribute: str, value: object)-> T:
        return cls(**Database.find_one(cls.COLLECTION, {attribute: value}))

    @classmethod
    def find_by_many(cls: Type[T], attribute: str, value: object)-> List[T]:
        return [cls(**element) for element in Database.find(cls.COLLECTION, {attribute: value})]

    @classmethod
    def get_by_id(cls: Type[T], _id: str)-> T:
        return cls.find_by_one("_id", _id)
