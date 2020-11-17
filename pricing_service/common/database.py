import pymongo as pym

from abc import abstractmethod, abstractclassmethod


class Database:
    URI = None
    DATABASE = None

    @classmethod
    def insert(cls, collection: str, data: str)-> None:
        cls.DATABASE[collection].insert(data)

    @classmethod
    def find_all(cls, collection: str, query: dict)-> pym.cursor:
        return cls.DATABASE[collection].find(query)

    @classmethod
    def find_one(cls, collection: str, query: dict)-> dict:
        return cls.DATABASE[collection].find_one(query)

    @classmethod
    def update(cls, collection: str, query: dict, data: dict)-> None:
        cls.DATABASE[collection].update(query, data, upsert=True)

    @classmethod
    def remove(cls, collection: str, query: dict)-> None:
        cls.DATABASE[collection].remove(query)


class DatabaseLocal(Database):
    URI = "mongodb://localhost:27017/pricing"
    DATABASE = pym.MongoClient(URI).get_database()
   
