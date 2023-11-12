import os
from motor.motor_asyncio import AsyncIOMotorClient

from pymongo import MongoClient

class MongoTools:
    _client = AsyncIOMotorClient('mongodb://192.168.0.123:27017/') #os.getenv("MONGODB_URL")
    _db = _client['library']

    @classmethod
    def get_client(cls):
        return cls._client

    @classmethod
    async def find(cls, collection: str, filter: dict):
        documents = cls._db[collection].find(filter)
        return documents
    
    @classmethod
    async def find_one(cls, collection: str, filter: dict):
        document = await cls._db[collection].find_one(filter)
        return document
    
    @classmethod
    async def insert_one(cls, collenction: str, document: dict):
        new_user = await cls._db[collenction].insert_one(document)
        return new_user
    
    @classmethod
    async def update_one(cls, collection: str, id: str, document: dict):
        update = await cls._db[collection].update_one(
            {'_id': id},
            {'$set': document}
        )
        return update
    
    @classmethod
    async def delete_one(cls, collection: str, id: str):
        result = await cls._db[collection].delete_one({'_id': id})
        return result
    
client = MongoClient('mongodb://192.168.0.123:27017/')
db = client["library"]